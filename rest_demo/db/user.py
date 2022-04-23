from rest_demo import db
from rest_demo.model.user import User
from rest_demo.package import utils


def create(user):
    user.setdefault('password', '')
    user['password'] = utils.ash_md5(user['password'])

    instance = User(**user)
    return db.create(instance)


def get(id):
    return db.get(User, id)


def list():
    return db.list(User)
