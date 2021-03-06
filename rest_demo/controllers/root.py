from pecan import expose

from rest_demo.controllers.v1 import v1Controller
from rest_demo.package import const


class RootController(object):

    @expose('json')
    def index(self):
        return {'version': const.VERSION}

    v1 = v1Controller()
