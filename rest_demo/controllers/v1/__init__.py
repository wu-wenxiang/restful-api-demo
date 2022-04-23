from pecan import expose

from rest_demo.controllers.v1 import user
from rest_demo.package import const


class v1Controller(object):
    users = user.UsersController()

    @expose('json')
    def index(self):
        return {'version': const.VERSION}
