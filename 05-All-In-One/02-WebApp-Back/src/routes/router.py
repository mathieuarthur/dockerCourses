from fastapi import FastAPI
from . import response, utils

def routing(app: FastAPI) -> None:
    app.include_router(response.router)
    app.include_router(utils.router)