from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from api.views.codes import Codes

api = Api()

api.add_resource(Codes, '/sql_codes')

db = SQLAlchemy()
migrate = Migrate()


def create_app(obj_config):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config[obj_config])
    api.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app
