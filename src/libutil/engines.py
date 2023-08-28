import os
from sqlalchemy import create_engine

from . import IS_TESTING


ENGINES = {}


def get_engine(engine_name):
    if engine_name in ENGINES:
        return ENGINES[engine_name]

    ENGINES[engine_name] = create_engine(
        'mysql+mysqldb://{username}:{password}@{host}/'.format(username=os.getenv("FOO_DB_USER"), password=os.getenv("FOO_DB_PASS"), host=os.getenv("FOO_DB_HOST")))  # TODO: work on
    return ENGINES[engine_name]


def get_engine_dev(engine_name, default_db=""):
    # test engine is used to create other DBs in
    # dev env, so it shouldn't have a default db
    if engine_name != "test":
        default_db = engine_name

    if engine_name in ENGINES:
        return ENGINES[engine_name]
    ENGINES[engine_name] = create_engine('mysql+mysqldb://root:root@mysql.default.svc.cluster.local/{}'.format(default_db))
    return ENGINES[engine_name]


if IS_TESTING:
    get_engine = get_engine_dev
