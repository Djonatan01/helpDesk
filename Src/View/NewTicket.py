from flask import Blueprint, render_template, request,redirect,url_for
#from flask_login import login_required
from ..Controller.Ticket import ControleTickets

tk = Blueprint('tk', __name__)

@tk.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        ControleTickets.cadastrarTicket(title,description)

        return redirect(url_for('router.home.index'))

    return render_template('new_ticket.html')
