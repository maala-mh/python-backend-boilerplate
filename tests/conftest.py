import os
os.environ["TESTING"] = "pytest"

import logging
import pytest

from jsql import sql

from libfoo import models, engine
from libutil import engines


logger = logging.getLogger(__name__)


class ObjProxy(object):
    def __init__(self, proxied, **kwargs):
        self._proxied = proxied
        self._kwargs = kwargs

    def __iter__(self):
        return self._proxied.__iter__()

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return getattr(self, attr)
        return getattr(self._proxied, attr)


class ClientProxy(ObjProxy):

    def post(self, url, *args, **kwargs):
        logger.warning("%s %s", url, kwargs.get('json'))
        assert_status = kwargs.pop('assert_status', 200)
        ret = ResponseProxy(self._proxied.post(url, *args, **kwargs))
        if assert_status:
            ret.assert_status(assert_status)
        return ret

    def get(self, url, *args, **kwargs):
        assert_status = kwargs.pop('assert_status', 200)
        ret = ResponseProxy(self._proxied.get(url, *args, **kwargs))
        if assert_status:
            ret.assert_status(assert_status)
        return ret


class ResponseProxy(ObjProxy):
    def assert_status(self, status_codes):
        status_codes = {status_codes} if isinstance(status_codes, int) else set(status_codes)
        assert self.status_code in status_codes, self.text


@pytest.fixture()
def client():
    from fastapi.testclient import TestClient
    from appfoo.views import router
    return ClientProxy(TestClient(router))


def setup_db():
    sql(engines.get_engine("test"), """
        CREATE DATABASE IF NOT EXISTS foo
    """)
    models.tables.create_all(engine)


setup_db()
