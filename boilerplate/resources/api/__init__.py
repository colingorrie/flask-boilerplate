from flask.ext.restful import Resource
from flask.ext.security import auth_token_required


class ProtectedResource(Resource):
    method_decorators = [auth_token_required]
