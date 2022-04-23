from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from rest_demo.model import Base
from rest_demo.model import user


def init_db():
    engine = create_engine(**config.sqlalchemy_w)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    admin = user.User(
        account='admin',
        name='Tom Cat',
        password='e10adc3949ba59abbe56e057f20f883e',
        email='tom.cat@test.com'
    )
    session.add(admin)
    session.commit()


init_db()
