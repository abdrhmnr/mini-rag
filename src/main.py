from src.routes.base import base_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(base_router)
