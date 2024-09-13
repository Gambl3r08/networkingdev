from fastapi import APIRouter, HTTPException
from app.schemas.ProductSchema import Product
from app.controllers.ProductController import ProductController
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.utils import StatusCodes
from typing import List


router = APIRouter()


@router.get("/products", response_model=List[Product])
async def get_products():
    try:
        products = ProductController().read_products()
        if products:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Products found",
                "data": products
            }
        else:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Product not created",
                "data": None
            }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: int):
    try:
        product = ProductController().read_product(product_id)
        if product:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Product found",
                "data": product
            }
        else:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "Product not created",
                "data": None
            }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products", response_model=Product)
async def create_product(product: Product):
    try:
        product = ProductController().create_product(product)
        response = {
            "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
            "message": "Product created",
            "data": product
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, product: Product):
    try:
        product = ProductController().update_product(product_id, product)
        response = {
            "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
            "message": "Product updated",
            "data": product
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
