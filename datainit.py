from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config
from rest_demo.model import Base
from rest_demo.model import book
from rest_demo.model import user
from rest_demo.package import utils


def init_db():
    engine = create_engine(**config.sqlalchemy_w)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    admin = user.User(
        account='admin',
        name='Tom Cat',
        password=utils.hash_md5('123456'),
        email='tom.cat@test.com'
    )
    session.add(admin)
    session.commit()
    session.refresh(admin)

    admin_book1 = book.Book(
        name='Book-1',
        user=admin
    )
    session.add(admin_book1)
    session.commit()


init_db()
