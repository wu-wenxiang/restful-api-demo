from rest_demo.tests import FunctionalTest


class TestUserController(FunctionalTest):

    def test_get(self):
        response = self.app.get('/v1/users')
        assert response.status_int == 200