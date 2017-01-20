from . import UnauthenticatedTestCase, AuthenticatedTestCase


class UnauthenticatedTest(UnauthenticatedTestCase):
    def test_get_thing_list_returns_401(self):
        response = self.client.get("/api/v1.0/things")
        self.assertEqual(response.status_code, 401)


class ThingListTest(AuthenticatedTestCase):
    def test_get_thing_list_returns_200(self):
        # pass headers=self.headers with every request for auth
        response = self.client.get("/api/v1.0/things", headers=self.headers)
        self.assertEqual(response.status_code, 200)
