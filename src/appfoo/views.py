from typing import Union
from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/mysql")
def test_mysql():
    from jsql import sql
    from sqlalchemy import create_engine
    engine = create_engine('mysql+mysqldb://root:root@mysql.default.svc.cluster.local/')
    with engine.begin() as conn:
        res = sql(conn, """
            SELECT * FROM test.Persons
        """).dicts()
    return {"res": res}
