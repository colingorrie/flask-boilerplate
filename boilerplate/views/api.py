from flask import Blueprint
from flask.ext.restful import Api
from boilerplate.resources.api.thing import ThingList


API_VERSION = 1.0

api_blueprint = Blueprint("api", __name__)

api = Api(api_blueprint, prefix="/api/v{}".format(API_VERSION))

api.add_resource(ThingList, "/things")
