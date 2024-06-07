from datetime import datetime
import logging
from Src.Model.Bd import Ticket
from config import db
from sqlalchemy.exc import IntegrityError

class ControleTickets():
    def cadastrarTicket( _title,_software, _description):
        data = datetime.now().strftime('%d/%m/%Y')
        hora = datetime.now().strftime('%H:%M:%S')
        tickets = Ticket(_title,_software,_description,'open',data,hora)

        db.session.add(tickets)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro: {e}")
            db.session.rollback()
        return False