from pecan import expose
from pecan.rest import RestController

from rest_demo.db import user as db_user


class TokensController(RestController):

    @expose('json')
    def post(self, user):
        return db_user.create(user)
