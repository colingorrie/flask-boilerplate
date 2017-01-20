from werkzeug.datastructures import Headers
from flask.ext.testing import TestCase
from boilerplate import create_app as _create_app
from boilerplate.auth import user_datastore
from boilerplate.models import User, Role


class BoilerplateTestCase(TestCase):
    def create_app(self):
        return _create_app(config="testing", instance_relative_config=True)


class DBFixtureTestCase(BoilerplateTestCase):
    def setUp(self):
        # populate database with fixture data
        pass

    def tearDown(self):
        # drop collections
        pass


class UserFixtureTestCase(DBFixtureTestCase):
    @classmethod
    def setUpClass(cls):
        user_datastore.create_user(email="test@example.com", password="sundown")

    @classmethod
    def tearDownClass(cls):
        User.drop_collection()
        Role.drop_collection()


class UnauthenticatedTestCase(DBFixtureTestCase):
    pass


class AuthenticatedTestCase(UserFixtureTestCase):
    def run(self, result=None):
        with self.client:
            self.client.post("/login", data=dict(email="test@example.com", password="sundown"))  # make sure session is correct
            token = user_datastore.get_user("test@example.com").get_auth_token()  #

            self.headers = Headers()
            self.headers.add("Authentication-Token", token)

            super().run(result)
