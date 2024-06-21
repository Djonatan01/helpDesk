from flask import Blueprint
from Src.View.Home import Home
from Src.View.NewTicket import tk
from Src.View.NewUser import User
from Src.View.Login import Login

Router = Blueprint('router', __name__)

Router.register_blueprint(Home)
Router.register_blueprint(tk)
Router.register_blueprint(User)
Router.register_blueprint(Login)