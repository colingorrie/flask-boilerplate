import nose
from flask.ext.script import Manager
from boilerplate import create_app
from boilerplate.auth import user_datastore


manager = Manager(create_app)
manager.add_option("-c", "--config", dest="config", required=False, default="testing")


@manager.command
def test(only=None):
    defaultTest = only or "."
    nose.main(argv=[""], defaultTest=defaultTest)


@manager.command
def create_user(email, password):
    user_datastore.create_user(email=email, password=password)


if __name__ == "__main__":
    manager.run()
