from flask.ext.testing import TestCase
from boilerplate import create_app as _create_app


class BoilerplateTestCase(TestCase):
    def create_app(self):
        return _create_app(config="testing", instance_relative_config=False)
