import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from libfoo import domain
from libutil import gcs
from libfoo.models import contracts


router = APIRouter()


@router.get("/headsortails/flip")
def flip_heads_or_tails():
    return HTMLResponse(content=domain.headsortails.flip_heads_or_tails(), status_code=200)


@router.get("/")
def get_heads_or_tails():
    return {"my response": "Hello World!"}


@router.get("/config")
def read_config(key):
    return {key: os.getenv(key)}


@router.get("/foo")
def get_foo_list():
    return domain.foo.get_foo_list()


@router.post("/foo")
def add_foo(payload: contracts.AddFoo):
    return domain.foo.add_foo(payload.email)


@router.get("/test-gcs")
def list_files_in_gcs(bucket_name: str):
    return gcs.list_blobs(bucket_name)
