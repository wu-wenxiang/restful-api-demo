from rest_demo import db
from rest_demo.model.book import Book
from rest_demo.model import Session

from sqlalchemy.orm import joinedload
from sqlalchemy import select


def create(book):
    instance = Book(**book)
    return db.create(instance)


def get(id):
    # TODO(wu.wenxiang) refact db.get
    # https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html
    stmt = select(Book).options(joinedload(Book.user)).where(Book.id == id)
    return Session.execute(stmt).scalars().one()
    # return db.get(query=query, id=id)


def list():
    return db.list(Book)


def delete(id):
    return db.delete(Book, id=id)
