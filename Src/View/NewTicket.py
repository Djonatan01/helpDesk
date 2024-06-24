from flask import Blueprint, render_template, request,redirect,url_for,send_file
from flask_login import login_required
from ..Controller.Ticket import ControleTickets
from Src.Model.Bd import Ticket
from sqlalchemy import desc
import pandas as pd
from io import BytesIO

tk = Blueprint('tk', __name__)

@tk.route('/new_ticket/<int:id>', methods=['GET','POST'])
@login_required
def new_ticket(id):
    if request.method == 'POST':

        tickets = Ticket.query.order_by(desc(Ticket.id)).first()

        if tickets:
            numTicket = tickets.id + 1
        else:
            numTicket = 1  # Se não houver nenhum ticket, começa do 1

        centroCusto = ''
        software_str=''
        description=''

        install_List = request.form.getlist('installsoftware')

        uninstall_List = request.form.getlist('uninstallsoftware')

        equipamento_List = request.form.getlist('equipamento')

        if len(install_List) > 0:
            software_str = ", ".join(install_List)
            valor = 'Instalação de Software'
            identificador = 'TS-IS-' + str(numTicket)

        if len(uninstall_List) > 0:
            software_str = ", ".join(uninstall_List)
            valor = 'Desinstalação de Software'
            identificador = 'TS-DS-' + str(numTicket)

        if len(equipamento_List) > 0:
            software_str = ", ".join(equipamento_List)
            centroCusto = request.form['centroCusto']
            valor = 'Compra de equipamento'
            identificador = 'TS-CE-' + str(numTicket)

        if len(install_List) == 0 and len(uninstall_List) == 0 and len(equipamento_List) == 0:
            valor = 'Atendimento Geral'
            identificador = 'TS-AG-' + str(numTicket)

        description = request.form['description']

        ControleTickets.cadastrarTicket(id,identificador,valor,software_str,description,centroCusto)
        return redirect(url_for('router.home.index'))

    return render_template('servico.html')


@tk.route('/servicos', methods=['GET','POST'])
@login_required
def servicos():
    tiket = request.form['numeroChamado']
    if tiket:
        # Filtrar tickets por número de chamado específico
        tickets = Ticket.query.filter_by(identificador=tiket).all()
    else:
        # Se nenhum número de chamado for fornecido, retornar todos os tickets
        tickets = Ticket.query.all()

    return render_template('servicos.html', tickets=tickets)

@tk.route('/tiket')
def tiket():
    tickets = Ticket.query.all()
    return render_template('servicos.html', tickets=tickets)


@tk.route('/<id>/atendimento')
def atendimento(id):
    tickets = Ticket.query.filter_by(id=id).all()
    return render_template('atendimento.html', tickets=tickets)

@tk.route('/update/<id>', methods=['GET','POST'])
@login_required
def update(id):
    Atendimento = request.form['Atendimento']
    status = request.form['status']
    idAtendenti = request.form['button']
    Atendimento = Atendimento +" | "+idAtendenti

    ControleTickets.atualizarTicket(id,status,Atendimento)

    return redirect(url_for('router.tk.tiket'))

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

@tk.route('/listar')
def listar():
    # Consultar todos os tickets
    tickets = Ticket.query.all()

    # Converter a lista de tickets para um DataFrame do pandas
    data = []
    for ticket in tickets:
        if ticket.status == 'open' or ' | ' not in ticket.execution:
            mensagem = ticket.execution
            atendente = ''
        else:
            mensagem, atendente = ticket.execution.split(' | ')

        data.append({
            'ID': ticket.id,
            'Identificador': ticket.identificador,
            'Título': ticket.title,
            'Software': ticket.software,
            'Descrição': ticket.description,
            'Mensagem': mensagem,
            'Atendente': atendente,
            'Status': ticket.status,
            'Centro de Custo': ticket.cost_center,
            'Data': ticket.created_data,
            'Hora': ticket.created_hora
        })

    df = pd.DataFrame(data)

    # Salvar o DataFrame em um arquivo Excel na memória
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Tickets')

    output.seek(0)

    # Enviar o arquivo Excel para o cliente
    return send_file(output, download_name="tickets.xlsx", as_attachment=True, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
