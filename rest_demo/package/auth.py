from datetime import datetime
from datetime import timedelta
import jwt
import logging
import os
from pecan import abort
from pecan import request
import re

from rest_demo.package.const import PUBLIC_URLS

JWT_KEY = "jwt_key"
SECRET_KEY = "SECRET_KEY"

logger = logging.getLogger(__name__)


def create_token(user_id):
    payload = {
        'exp': (datetime.now() + timedelta(minutes=60)).timestamp(),
        'user_id': user_id
    }
    key = os.getenv(JWT_KEY) or SECRET_KEY
    return jwt.encode(payload, key, algorithm='HS256')


def decode_token(jwt_token):
    token = {}
    secret = os.getenv(JWT_KEY) or SECRET_KEY
    try:
        token = jwt.decode(jwt_token, secret, algorithms=['HS256'])
    except Exception as e:
        logger.info(f'invalid token ({jwt_token}): {e}')
        abort(401, f'invalid token ({jwt_token}): {e}')
    return token


public_urls = [
    {'method': i[0], 'url': re.compile(i[1], re.IGNORECASE)}
    for i in PUBLIC_URLS
]


def assert_login(state_request):
    if any(
        i['method'] == state_request.method and i['url'].search(
            state_request.path) for i in public_urls
    ):
        return

    token = request.cookies.get('token')
    token = decode_token(token)
    if not token:
        abort(401, 'Please signin.')
    state_request.token = token


def assert_permission(state_request):
    pass
    # TODO(wu.wenxiang)
