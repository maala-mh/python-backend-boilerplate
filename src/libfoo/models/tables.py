import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


logger = logging.getLogger(__name__)

Base = declarative_base()


def create_all(engine):
    Base.metadata.create_all(bind=engine)


class Foo(Base):
    __tablename__ = "foo"

    id_foo = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique=True, index=True)
    is_active = Column(Boolean, default=True)
