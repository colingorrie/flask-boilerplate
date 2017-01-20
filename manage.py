import nose
from flask.ext.script import Manager
from boilerplate import create_app


manager = Manager(create_app)
manager.add_option("-c", "--config", dest="config", required=False, default="testing")


@manager.command
def test(only=None):
    defaultTest = only or "."
    nose.main(argv=[""], defaultTest=defaultTest)


if __name__ == "__main__":
    manager.run()
