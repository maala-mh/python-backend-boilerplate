from fastapi import APIRouter

from libfoo import domain
from libfoo.models import contracts


router = APIRouter()


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/foo")
def get_foo_list():
    return domain.foo.get_foo_list()


@router.post("/foo")
def add_foo(payload: contracts.AddFoo):
    return domain.foo.add_foo(payload.email)
