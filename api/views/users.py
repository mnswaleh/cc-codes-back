from flask_restplus import Resource
from models.users import User


class Users(Resource):
    def post(self):
        current_user = User.repr()
        return {'hello': current_user}
