from src.routes.base import base_router
from src.routes import data
from fastapi import FastAPI


app = FastAPI()

app.include_router(base_router)
app.include_router(data.data_router)
