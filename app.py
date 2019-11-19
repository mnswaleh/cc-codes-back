from flask import Flask
from flask_restplus import Api
from config import config
from api.views.codes import Codes

api = Api()

api.add_resource(Codes, '/sql_codes')

def create_app(obj_config):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config[obj_config])
    api.init_app(app)

    return app
