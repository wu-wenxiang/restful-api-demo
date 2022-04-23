from pecan import expose

from rest_demo.controllers.user import UsersController
from rest_demo.package import const


class RootController(object):

    @expose('json')
    def index(self):
        return {'version': const.VERSION}

    users = UsersController()
