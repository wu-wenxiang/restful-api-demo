import logging
from pecan import abort
from sqlalchemy.orm import exc
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


@try_db
def get(model=None, query=None, **kwargs):
    if query is None:
        query = Session.query(model)
    return query.filter_by(**kwargs).one()


@try_db
def try_get(model, **kwargs):
    query = Session.query(model)
    return query.filter_by(**kwargs).one_or_none()


@try_db
def list(model, **kwargs):
    query = Session.query(model)
    return query.filter_by(**kwargs).all()


@try_db
def delete(model, **kwargs):
    Session.query(model).filter_by(**kwargs).delete(
        synchronize_session="fetch")
