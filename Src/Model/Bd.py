from datetime import datetime
from config import db

# ***************************************User Sistem************************************************


class CreatUser(db.Model):
    __tablename__ = "Usuarios"
    idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.Text, nullable=False)
    fone = db.Column(db.Text, nullable=False)
    emailUser = db.Column(db.Text, nullable=False)
    passwordUser = db.Column(db.Text, nullable=False)

    def __init__(self, _userName,_fone, _emailUser, _passwordUser):
        self.userName
        self.fone
        self.emailUser
        self.passwordUser

# ***************************************Tickets Sistem*********************************************


class Ticket(db.Model):
    __tablename__ = "Ticket"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idUser = db.Column(db.Integer,db.ForeignKey('Usuarios.idUser'))
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