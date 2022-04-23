from rest_demo.tests import FunctionalTest


class TestV1Controller(FunctionalTest):

    def test_get(self):
        response = self.app.get('/v1/')
        assert response.status_int == 200
