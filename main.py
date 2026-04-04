from routes.base import base_router
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv(".env")

app = FastAPI()

app.include_router(base_router)
