import logging

logger = logging.getLogger(__name__)

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
