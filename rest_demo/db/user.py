from rest_demo import db
from rest_demo.model import Session
from rest_demo.model.user import User
from rest_demo.package import utils

# from sqlalchemy.orm import joinedload
from sqlalchemy import select


def create(user):
    user.setdefault('password', '')
    user['password'] = utils.hash_md5(user['password'])

    instance = User(**user)
    return db.create(instance)


def get(id):
    filters = (User.id == id,)
    return db.get(model=User, filters=filters)


def list():
    return db.list(model=User)


def delete(id):
    filters = (User.id == id,)
    db.delete(model=User, filters=filters)
