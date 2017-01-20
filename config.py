class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    MONGODB_HOST = "wherever.com"
    MONGODB_PORT = 12345
    MONGODB_DB = "boilerplate-prod"


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "boilerplate-dev"


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    LIVESERVER_PORT = 8943
    MONGODB_HOST = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "boilerplate-test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
