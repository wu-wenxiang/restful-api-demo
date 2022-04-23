from pecan import conf
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


Session = scoped_session(sessionmaker())
metadata = MetaData()


def _engine_from_config(configuration):
    configuration = dict(configuration)
    url = configuration.pop('url')
    return create_engine(url, **configuration)


def init_model():
    conf.sqlalchemy.engine = _engine_from_config(conf.sqlalchemy)


def start():
    Session.bind = conf.sqlalchemy.engine
    metadata.bind = Session.bind


def commit():
    Session.commit()


def rollback():
    Session.rollback()


def clear():
    Session.remove()
