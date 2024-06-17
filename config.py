import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#from flask_login import LoginManager

template_dir = os.path.abspath('./Templates')

app = Flask(__name__,
            template_folder=template_dir,
            static_url_path="/Public",
            static_folder='Public')

app.config["SECRET_KEY"] = 'Proj_Governanca_TI'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///helpdesk.sqlite3'
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

# login_manager = LoginManager()
# login_manager.login_view = 'router.login.login'
# login_manager.login_message = 'Realize o login para acessar essa página!'
# login_manager.init_app(app)


@app.route('/apply-migrations')
def apply_migrations():
    try:
        # Verifica se há migrações pendentes
        migrate.upgrade(directory='alembic/versions')
        return "Migrações aplicadas com sucesso."
    except Exception as e:
        return f"Erro ao aplicar migrações: {str(e)}"