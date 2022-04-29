from os import abort
from rest_demo import db
from rest_demo.model.user import User
from rest_demo.package import auth
from rest_demo.package import utils


def get_user_by_account(account, password):
    password = utils.hash_md5(password)
    filters = (User.account == account, User.password == password)
    user = db.try_get(model=User, filters=filters)
    if not user:
        abort(401, f'invalid user or wrong password')
    return user


def get_user_by_token(token):
    token = auth.decode_token(token)
    user_id = token['user_id']
    filters = (User.id == user_id,)
    user = db.try_get(model=User, filters=filters)
    if not user:
        abort(401, f'invalid user')
    return user
