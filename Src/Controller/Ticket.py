from datetime import datetime
import logging
from Src.Model.Bd import Ticket
from config import db
from sqlalchemy.exc import IntegrityError

class ControleTickets():
    def cadastrarTicket(_title, _description):
        data = datetime.now().strftime('%d/%m/%Y')
        tickets = Ticket(_title,_description,' ',data)

        db.session.add(tickets)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro: {e}")
            db.session.rollback()
        return False