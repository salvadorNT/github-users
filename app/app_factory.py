from flask import Flask
from flask_restful import Api

from .views.main_api import UserList
from .models.core import db
from . import views


def register_blueprints_on_app(app):
    """Registers the routes of app's views"""
    app.register_blueprint(views.main_pages)
    app.register_blueprint(views.main_api, url_prefix='/api')


def create_app(register_blueprints=True):
    """Function to instantiate, configure, and return a flask app"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('app.default_config')  # default config
    # app.config.from_pyfile('application.cfg.py')  # server config file, do not include in versioning

    db.init_app(app)
    api = Api(app)
    api.add_resource(UserList, '/api/users')

    if register_blueprints:
        register_blueprints_on_app(app)

    return app
