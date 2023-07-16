from typing import Union

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/mysql/hc")
def mysql_hc():
    from sqlalchemy import create_engine
    from sqlalchemy import text
    # mysql + mysqldb: // root: root @ mysql.default.svc.cluster.local / invoice
    stt = """
        CREATE DATABASE test;
        CREATE TABLE test.Persons (
            PersonID int,
            LastName varchar(255),
            FirstName varchar(255),
            Address varchar(255),
            City varchar(255)
        );
    """
    engine = create_engine("mysql+mysqldb://root:root@mysql.default.svc.cluster.local")
    with engine.connect() as connection:
        result = connection.execute(text(stt))
    return {"result": result}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
