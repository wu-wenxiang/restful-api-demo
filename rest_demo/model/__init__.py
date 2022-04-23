from pecan import conf
from sqlalchemy import create_engine
from sqlalchemy.ext import declarative
from sqlalchemy import MetaData
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

Session = scoped_session(sessionmaker())
metadata = MetaData()
Base = declarative.declarative_base()


def init_model():
    conf.sqlalchemy_w.engine = _engine_from_config(conf.sqlalchemy_w)
    conf.sqlalchemy_ro.engine = _engine_from_config(conf.sqlalchemy_ro)


def _engine_from_config(configuration):
    configuration = dict(configuration)
    url = configuration.pop('url')
    return create_engine(url, **configuration)


def start():
    Session.bind = conf.sqlalchemy_w.engine
    metadata.bind = conf.sqlalchemy_w.engine


def start_read_only():
    Session.bind = conf.sqlalchemy_ro.engine
    metadata.bind = conf.sqlalchemy_ro.engine


def commit():
    Session.commit()


def rollback():
    Session.rollback()


def clear():
    Session.close()


def flush():
    Session.flush()
