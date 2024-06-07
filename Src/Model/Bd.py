from datetime import datetime
from config import db

# ***************************************User Sistem************************************************


class CreatUser(db.Model):
    __tablenam__ = "Usuarios"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nomeUser = db.Column(db.Text, nullable=False)
    emailUser = db.Column(db.Text, nullable=False)
    senhaUser = db.Column(db.Text, nullable=False)

    def __init__(self, _id, _nomeUser, _emailUser, _senhaUser):
        self.nomeUser
        self.emailUser
        self.senhaUser

# ***************************************Tickets Sistem*********************************************


class Ticket(db.Model):
    __tablename__ = "Ticket"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    software=db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Open')
    created_data = db.Column(db.String, nullable=False)
    created_hora = db.Column(db.String, nullable=False)

    def __init__(self, _title,_software, _description, _status, _created_data,_created_hora):
        self.title = _title
        self.software = _software
        self.description = _description
        self.status = _status
        self.created_data = _created_data
        self.created_hora = _created_hora
