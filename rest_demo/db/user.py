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
    # TODO(wu.wenxiang) joinload not work in select
    # https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html
    stmt = select(User).where(User.id == id)
    return Session.execute(stmt).scalars().one()
    # return db.get(query=query, id=id)


def list():
    return db.list(User)


def delete(id):
    return db.delete(User, id=id)
