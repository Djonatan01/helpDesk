from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..Controller.User import CreatUsers
from Src.Model import Regex
from werkzeug.security import generate_password_hash

User = Blueprint('user', __name__)

@User.route('/createUser', methods=['GET', 'POST'])
def createUser():
    userName = request.form.get('userName')
    fone = request.form.get('userFone')
    emailUser = request.form.get('userEmail')
    passwordUser = request.form.get('userpassword')

    if request.method == 'POST':
        if CreatUsers.checkEmail(_email = emailUser):
            flash('Email já cadastrado', 'error')
        else:
            if Regex.contatoRegex(fone):
                if Regex.emailRegex(emailUser):
                    if CreatUsers.creatUsersname(userName, fone, emailUser, passwordUser):
                        return redirect(url_for('router.login.login'))
                else:
                    flash('E-mail inválido', 'error')
            else:
                flash('Celular inválido', 'error')

    return render_template('criarUsuarios.html')













# @User.route('/<int:id>/updateUser', methods=['GET', 'POST'])
# @login_required
# def updateUser(id):
#     _user = Usuarios.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         _cpf = request.form.get('cpf')
#         _nome = request.form.get('nome')
#         _endereco = request.form.get('endereco')
#         _contato = request.form.get('contato')
#         _email = request.form.get('email')
#         if any((x is None or len(x) < 1) for x in [_cpf, _nome, _endereco, _contato, _email]):
#             flash('Preencha todos os campos do formulário', 'error')
#         else:
#             if UserController.updateUser(id, _cpf, _user.codUser, _nome, _endereco, _contato, _email, _user.status):
#                 return redirect(url_for('router.user.listUser'))
#             else:
#                 flash('Usuário já cadastrado', 'error')
#     return render_template('atualizarUsuarios.html', user=_user)


# @User.route('/<int:id>/removeUser', methods=['GET', 'POST'])
# @login_required
# def removeUser(id):
#     UserController.removeUser(id)
#     return redirect(url_for('router.user.listUser'))