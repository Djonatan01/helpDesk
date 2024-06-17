from flask import Blueprint, render_template, request,redirect,url_for
#from flask_login import login_required
from ..Controller.Ticket import ControleTickets

tk = Blueprint('tk', __name__)

@tk.route('/new_ticket', methods=['POST'])
def new_ticket():
    if request.method == 'POST':
        install_List = request.form.getlist('installsoftware')

        uninstall_List = request.form.getlist('uninstallsoftware')

        if len(install_List) > 0:
            software_str = ", ".join(install_List)
            valor = 'Instalação de Software'

        if len(uninstall_List) > 0:
            software_str = ", ".join(uninstall_List)
            valor = 'Desinstalação de Software'

        description = request.form['description']
        ControleTickets.cadastrarTicket(valor,software_str,description)
        return redirect(url_for('router.home.index'))

    return render_template('servico.html')


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