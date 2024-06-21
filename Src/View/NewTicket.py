from flask import Blueprint, render_template, request,redirect,url_for
from flask_login import login_required
from ..Controller.Ticket import ControleTickets
from Src.Model.Bd import Ticket

tk = Blueprint('tk', __name__)

@tk.route('/new_ticket', methods=['POST'])
@login_required
def new_ticket():
    if request.method == 'POST':
        centroCusto = ''
        software_str=''
        description=''

        install_List = request.form.getlist('installsoftware')

        uninstall_List = request.form.getlist('uninstallsoftware')

        equipamento_List = request.form.getlist('equipamento')

        if len(install_List) > 0:
            software_str = ", ".join(install_List)
            valor = 'Instalação de Software'

        if len(uninstall_List) > 0:
            software_str = ", ".join(uninstall_List)
            valor = 'Desinstalação de Software'

        if len(install_List) == 0 and len(uninstall_List) == 0:
            valor = 'Atendimento Geral'

        if len(equipamento_List) > 0:
            centroCusto = request.form['centroCusto']
            valor = 'Compra de equipamento'

        description = request.form['description']

        ControleTickets.cadastrarTicket(valor,software_str,description,centroCusto)
        return redirect(url_for('router.home.index'))

    return render_template('servico.html')

@tk.route('/servicos')
def servicos():
    tickets = Ticket.query.all()
    return render_template('servicos.html', tickets=tickets)

@tk.route('/servico/<tipo>')
@login_required
def servico(tipo):
    # Lógica para lidar com diferentes tipos de serviços
    if tipo == 'install_software':
        return render_template('servico.html', titulo="Instalação de Software", tipo=tipo)
    elif tipo == 'uninstall_software':
        return render_template('servico.html', titulo="Desinstalação de Software", tipo=tipo)
    elif tipo == 'general_support':
        return render_template('servico.html', titulo="Atendimento em Geral", tipo=tipo)
    elif tipo == 'equipment_purchase':
        return render_template('servico.html', titulo="Solicitação de Compra de Equipamento de TI", tipo=tipo)
    else:
        return render_template('404.html'), 404