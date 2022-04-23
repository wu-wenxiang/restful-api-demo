# from datetime import datetime
# from sqlalchemy import Boolean
from sqlalchemy import Column
# from sqlalchemy import DateTime
# from sqlalchemy import ForeignKey
from sqlalchemy import Integer
# from sqlalchemy import JSON
from sqlalchemy.orm import deferred
# from sqlalchemy.orm import relationship
from sqlalchemy import String
# from sqlalchemy import Table
# from sqlalchemy.types import Date
# from sqlalchemy import UniqueConstraint

from . import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    account = Column(String(64), unique=True)
    name = Column(String(64), nullable=False)
    password = deferred(Column(String(64), nullable=False))
    email = Column(String(128))
