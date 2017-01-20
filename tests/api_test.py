from . import BoilerplateTestCase


class SomethingTest(BoilerplateTestCase):
    def test_get_something_returns_200(self):
        response = self.client.get("/api/v1.0/something")
        self.assertEqual(response.status_code, 200)
