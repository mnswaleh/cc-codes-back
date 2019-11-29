from flask_restplus import Resource


class Codes(Resource):
    def get(self):
        return {'hello': 'world'}
