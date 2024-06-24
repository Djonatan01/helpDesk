from datetime import datetime
import logging
from Src.Model.Bd import Ticket
from config import db
from sqlalchemy.exc import IntegrityError

class ControleTickets():
    def cadastrarTicket(idUser,_identificador, _title,_software, _description,_centroCusto):
        data = datetime.now().strftime('%d/%m/%Y')
        hora = datetime.now().strftime('%H:%M:%S')

        tickets = Ticket(idUser,_identificador,_title,_software,_description,'open','',data ,hora, _centroCusto)

        db.session.add(tickets)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro: {e}")
            db.session.rollback()
        return False

    def atualizarTicket(_id,_status,_atendimento):
        # Consulta o ticket baseado no _id
        ticket = db.session.query(Ticket).filter_by(id=_id).first()
        if ticket:
            # Atualiza os campos desejados
            ticket.status = _status
            ticket.execution = _atendimento

            # Tenta comitar as mudanças
            try:
                db.session.commit()
                return True
            except IntegrityError as e:
                logging.error(f"Ocorreu um erro: {e}")
                db.session.rollback()
                return False