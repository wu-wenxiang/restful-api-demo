from rest_demo.package.auth import create_token
from rest_demo.tests import FunctionalTest


class TestUserController(FunctionalTest):
    def test_list(self):
        # TODO(wu.wenxiang) post json 带参数
        jwt_token = create_token(user_id=1)

        response = self.app.get(
            '/v1/users',
            headers={'cookie': f'token={jwt_token}'}
        )
        assert response.status_int == 200
