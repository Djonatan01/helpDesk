from config import db
from flask_login import UserMixin

# ***************************************User Sistem************************************************

class CreatUser(UserMixin,db.Model):
    __tablename__ = "CreatUser"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(150), nullable=False)
    fone = db.Column(db.String(50), nullable=False)
    cadDate = db.Column(db.String(50), nullable=False)
    hour = db.Column(db.String(10), nullable=False)
    emailUser = db.Column(db.String(150), nullable=False)
    passwordUser = db.Column(db.String, nullable=False)

    def __init__(self, _userName,_fone,_cadDate,_hour,_emailUser, _passwordUser):
        self.userName=_userName
        self.fone=_fone
        self.cadDate=_cadDate
        self.hour=_hour
        self.emailUser=_emailUser
        self.passwordUser=_passwordUser

# ***************************************Tickets Sistem*********************************************


class Ticket(db.Model):
    __tablename__ = "Ticket"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUser = db.Column(db.Integer,db.ForeignKey('CreatUser.id'))
    title = db.Column(db.String(50), nullable=False)
    software = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Open')
    execution = db.Column(db.String(500), nullable=False)
    created_data = db.Column(db.String, nullable=False)
    created_hora = db.Column(db.String, nullable=False)
    cost_center = db.Column(db.String, nullable=False)

    def __init__(self, _idUser, _title, _software, _description, _status,_execution, _created_data, _created_hora,_cost_center):
        self.idUser = _idUser
        self.title = _title
        self.software = _software
        self.description = _description
        self.status = _status
        self.execution = _execution
        self.created_data = _created_data
        self.created_hora = _created_hora
        self.cost_center = _cost_center