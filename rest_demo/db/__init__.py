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
def get(model, id):
    query = Session.query(model)
    return query.filter_by(id=id).one()


@try_db
def list(model):
    query = Session.query(model)
    return query.all()


@try_db
def delete(model, id):
    Session.query(model).filter_by(id=id).delete(synchronize_session="fetch")
