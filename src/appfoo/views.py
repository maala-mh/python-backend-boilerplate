import os
from fastapi import APIRouter

from libfoo import domain
from libfoo.models import contracts


router = APIRouter()


@router.get("/")
def read_root():
    return {"my response": "Hello World!"}


@router.get("/config")
def read_config(key):
    return {key: os.getenv(key)}


@router.get("/foo")
def get_foo_list():
    return domain.foo.get_foo_list()


@router.get("/create-table")
def create_table(query):
    return domain.foo.create_table(query)


@router.post("/foo")
def add_foo(payload: contracts.AddFoo):
    return domain.foo.add_foo(payload.email)
