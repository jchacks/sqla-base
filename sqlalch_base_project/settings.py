import atexit
import logging

logger = logging.getLogger(__name__)

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool


SQL_ALCHEMY_CONN = 'sqlite:////tmp/tmp.db'


engine = None
Session = None


def configure_orm():
    global engine
    global Session
    engine_args = {}
    engine_args['poolclass'] = NullPool
    engine = create_engine(SQL_ALCHEMY_CONN, **engine_args)

    Session = scoped_session(
        sessionmaker(autocommit=False,
                     autoflush=False,
                     bind=engine,
                     expire_on_commit=False))


def dispose_orm():
    """ Properly close pooled database connections """
    global engine
    global Session

    if Session:
        Session.remove()
        Session = None
    if engine:
        engine.dispose()
        engine = None


configure_orm()


@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


atexit.register(dispose_orm)
