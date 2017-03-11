from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    # Initialize app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    # Initialze db
    db.init_app(app)

    # Initialize login manager
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    return app
