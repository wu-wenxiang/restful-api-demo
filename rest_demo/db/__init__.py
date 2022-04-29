import logging
from pecan import abort
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy.orm import exc
from sqlalchemy import select
from webob.exc import WSGIHTTPException

from rest_demo.model import Session

logger = logging.getLogger(__name__)


def try_db(func):
    def wapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except exc.NoResultFound as e:
            errMsg = f'{func.__name__}({args}, {kwargs}): {e}'
            logger.warning(errMsg)
            abort(404, errMsg)
        except WSGIHTTPException as e:
            errMsg = f'{func.__name__}({args}, {kwargs}): {e}'
            logger.warning(errMsg)
            abort(e.code, errMsg)
        except Exception as e:
            errMsg = f'{func.__name__}({args}, {kwargs}): {e}'
            logger.error(errMsg)
            abort(409, errMsg)
    wapper.__name__ = func.__name__
    return wapper


@try_db
def create(instance):
    Session.add(instance)
    Session.commit()
    Session.refresh(instance)
    return instance


# https://docs.sqlalchemy.org/en/14/tutorial/orm_related_objects.html
def _get(model=None, query=None, filters=()):
    if query is None:
        query = select(model)
        for filter in filters:
            query = query.where(filter)
    return Session.execute(query).scalars()


@try_db
def get(model=None, query=None, filters=()):
    return _get(model, query, filters).one()


@try_db
def try_get(model=None, query=None, filters=()):
    return _get(model, query, filters).one_or_none()


@try_db
def list(model=None, query=None, filters=()):
    return _get(model, query, filters).all()


# https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html?highlight=delete#orm-enabled-delete-statements
@try_db
def delete(model=None, query=None, filters=()):
    if query is None:
        query = sqlalchemy_delete(model)
        for filter in filters:
            query = query.where(filter)
    Session.execute(query)
