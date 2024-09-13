from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.db import init_db
from app.services.ProductService import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
app = FastAPI(lifespan=lifespan)

app.include_router(
    product_router, tags=["Products"], prefix="/api/v1")
