import logging

from jsql import sql

from libfoo import engine


logger = logging.getLogger(__name__)


def add_foo(email):
    sql(engine, """INSERT IGNORE INTO foo.foo (email) VALUES (:email)""", email=email)


def get_foo_list():
    foo_list = sql(engine, """
        SELECT *
        FROM foo.foo
    """).dicts()

    return foo_list
