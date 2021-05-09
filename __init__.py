from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

database = SQLAlchemy()
DB_NAME = "office_management.db"
# DB_USERNAME = 'root'
# DB_PASSWORD = 'password'

def create_app():
    app = Flask(__name__ )
    app.config['SECRET_KEY'] = 'AHFGASDHFBASHDFBHDFBFBDJKASDFJKASDFJKASDFB2314324'

    # database configurarion
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    
    # initialize connection
    database.init_app(app)

    from .routes.views import views
    from .routes.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    from .models import Employee
    from .models import Salary

    create_database(app)
    
    login_manager =  LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/'+DB_NAME):
        database.create_all(app=app)
        print('database created')