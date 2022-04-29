from rest_demo import db
from rest_demo.model.book import Book

from sqlalchemy.orm import joinedload
from sqlalchemy import select


def create(book):
    instance = Book(**book)
    return db.create(instance)


def get(id):
    query = select(Book).options(joinedload(Book.user)).where(Book.id == id)
    return db.get(query=query)


def list():
    return db.list(model=Book)


def delete(id):
    db.delete(model=Book, filters=(Book.id == id,))
