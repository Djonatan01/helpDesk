from datetime import datetime
import logging
from Src.Model.Bd import CreatUser
from config import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

class CreatUsers:
    def creatUsersname(_userName,_fone, _emailUser, _passwordUser):
        data = datetime.now().strftime('%d/%m/%Y')
        hora = datetime.now().strftime('%H:%M:%S')
        passwordUser = generate_password_hash(_passwordUser)
        craetUsers = CreatUser(_userName,_fone,data,hora,_emailUser,passwordUser)

        db.session.add(craetUsers)
        try:
            db.session.commit()
            return True
        except IntegrityError as e:
            logging.error(f"Ocorreu um erro: {e}")
            db.session.rollback()
        return False
    def checkEmail(_email):
        query = CreatUser.query.filter_by(emailUser=_email).first()
        return False if query == None or query == 'None' else True