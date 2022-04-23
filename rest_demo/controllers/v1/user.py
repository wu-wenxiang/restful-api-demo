from pecan import expose
from pecan.rest import RestController

from rest_demo.db import user as db_user


class UsersController(RestController):

    @expose('json')
    def get_one(self, id):
        return db_user.get(id)

    @expose('json')
    def get_all(self):
        return db_user.list()

    @expose('json')
    def post(self, user):
        return db_user.create(user)

    @expose('json')
    def delete(self, id):
        return db_user.delete(id)
