import logging

from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from fastapi.requests import Request


logger = logging.getLogger(__name__)
SVC_NAME = "foo"

app_params = {
    "title": f"{SVC_NAME} public API",
    "description": f"{SVC_NAME} public api",
    "version": "0.1.0",
    "docs_url": "/swagger",
    "redoc_url": "/docs",
}
app = FastAPI(**app_params)


@app.middleware("http")
async def before_request(request: Request, call_next):
    return await call_next(request)


from appfoo.views import router

app.include_router(router)
app = SentryAsgiMiddleware(app)
