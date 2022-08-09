from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = getenv("DATABASE_URL")
assert database_url is not None

engine = create_engine(
    database_url,
    echo=True,  # for development only
    connect_args={"connect_timeout": 3},
    pool_pre_ping=True
)

DBSession = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


def initialize_sql(eng):
    Base.metadata.bind = eng
    Base.metadata.create_all(eng)
