from flask import Blueprint, render_template
from Src.Model.Bd import Ticket

Home = Blueprint('home', __name__)

@Home.route('/')
@Home.route('/home')
def index():
#  tickets = Ticket.query.all()
  #return render_template('index.html', tickets=tickets)
  return render_template('index.html')
