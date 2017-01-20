from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
from .models import db
from .views.blueprint import blueprint


environments = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
}


def create_app(config=None, instance_relative_config=True):
    app = Flask(__name__, instance_relative_config=instance_relative_config)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.url_map.strict_slashes = False

    if config in environments:
        app.config.from_object(environments.get(config))
    else:  # default to development config
        print("No config '{}'. Defaulting to config 'development'.".format(config))
        app.config.from_object("config.DevelopmentConfig")

    if instance_relative_config:
        app.config.from_pyfile("config.py")  # instance-based config

        if app.config["MONGODB_HOST"] == "localhost":
            # no password if we're using localhost
            del(app.config["MONGODB_USERNAME"])
            del(app.config["MONGODB_PASSWORD"])

    db.init_app(app)

    app.register_blueprint(blueprint)

    return app
