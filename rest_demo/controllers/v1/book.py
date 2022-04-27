from pecan import expose
from pecan.rest import RestController

from rest_demo.db import book as db_book


class BooksController(RestController):

    @expose('json')
    def get_one(self, id):
        return db_book.get(id)

    @expose('json')
    def get_all(self):
        return db_book.list()

    @expose('json')
    def post(self, book):
        return db_book.create(book)

    @expose('json')
    def delete(self, id):
        return db_book.delete(id)
