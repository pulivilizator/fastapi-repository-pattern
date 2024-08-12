from fastapi import FastAPI

from application.routers import get_routers

app = FastAPI()

[app.include_router(router) for router in get_routers()]