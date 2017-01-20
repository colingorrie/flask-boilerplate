from flask.ext.restful import Resource
from flask.ext.restful.reqparse import RequestParser
from boilerplate.util import autoreconnect


class Something(Resource):
    def __init__(self):
        super().__init__()

        self.parser = RequestParser()

        # self.parser.add_argument("id", type=int)  # add arguments for post, patch

    @autoreconnect
    def get(self):
        # connect this to model
        return [], 200
