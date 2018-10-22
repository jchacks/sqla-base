import logging

logger = logging.getLogger(__name__)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalch_base_project.utils.db import provide_session

Base = declarative_base()


# Example models

class Setting(Base):
    __tablename__ = 'setting'

    name = Column(String(50), primary_key=True)
    value = Column(String(1024))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250), nullable=False)

    @classmethod
    @provide_session
    def all(cls, session=None):
        session.query(cls).all()