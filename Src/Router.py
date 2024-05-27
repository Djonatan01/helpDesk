from flask import Blueprint
from Src.View.Home import Home
from Src.View.NewTicket import tk

Router = Blueprint('router', __name__)

Router.register_blueprint(Home)
Router.register_blueprint(tk)
