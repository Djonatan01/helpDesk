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
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Open')
    created_at = db.Column(db.String, nullable=False)

    def __init__(self, _title, _descriptio, _status, _created_at):
        self.title = _title
        self.description = _descriptio
        self.status = _status
        self.created_at = _created_at
