from sqlalchemy import create_engine

from . import IS_TESTING


ENGINES = {}


def get_engine(engine_name):
    if engine_name in ENGINES:
        return ENGINES[engine_name]
    ENGINES[engine_name] = create_engine('mysql+mysqldb://root:root@mysql.default.svc.cluster.local/')  # TODO: work on
    return ENGINES[engine_name]


def get_engine_dev(engine_name):
    if engine_name in ENGINES:
        return ENGINES[engine_name]
    ENGINES[engine_name] = create_engine('mysql+mysqldb://root:root@mysql.default.svc.cluster.local/test')
    return ENGINES[engine_name]


if IS_TESTING:
    get_engine = get_engine_dev
