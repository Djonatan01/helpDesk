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


@tk.route('/servico/<tipo>')
def servico(tipo):
    # Lógica para lidar com diferentes tipos de serviços
    if tipo == 'install_software':
        return render_template('servico.html', titulo="Instalação de Software", tipo=tipo)
    elif tipo == 'uninstall_software':
        return render_template('servico.html', titulo="Desinstalação de Software", tipo=tipo)
    elif tipo == 'general_support':
        return render_template('servico.html', titulo="Atendimento em Geral", tipo=tipo)
    elif tipo == 'equipment_purchase':
        return render_template('servico.html', titulo="Compra de Equipamentos", tipo=tipo)
    else:
        return render_template('404.html'), 404