from pecan import abort
from pecan import expose
from pecan.rest import RestController
from rest_demo.db.token import get_user_by_account
from rest_demo.db.token import get_user_by_token
from rest_demo.package.auth import create_token

AUTH_METHODS = {
    'password': get_user_by_account,
    'token': get_user_by_token
}


class TokensController(RestController):

    @expose('json')
    def post(self, auth):
        methods = auth.get('methods', [])

        if not set() < set(methods) <= set(AUTH_METHODS):
            abort(401, (
                f'invalid methods ({methods}), methods should not be emtpy,'
                f'and should in ({set(AUTH_METHODS)}) sets.'
            ))

        for method in methods:
            kwargs = auth.get(method, {})
            try:
                user = AUTH_METHODS[method](**kwargs)
            except Exception as e:
                abort(401, f'invalid credential ({kwargs}), {e}')

        return {'token': create_token(user.id)}
