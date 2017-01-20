class Config(object):
    DEBUG = False
    TESTING = False
    SECURITY_LOGIN_URL = "/api/v1.0/login"
    SECURITY_LOGOUT_URL = "/api/v1.0/logout"
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = False
    WTF_CSRF_ENABLED = False


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
