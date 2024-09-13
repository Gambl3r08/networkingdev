from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends
from sqlmodel import Session

from database.crud import create_product, read_product, read_products
from database.db import init_db, get_session
from database.models import Product


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

