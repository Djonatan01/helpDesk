from config import db, app
from Src.Router import Router

app.register_blueprint(Router)

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()

app.run(debug=True)
