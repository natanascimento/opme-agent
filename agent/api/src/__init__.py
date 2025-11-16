from fastapi import FastAPI

from routes.hooks import router

api = FastAPI()

api.include_router(router)