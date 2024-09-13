from fastapi import APIRouter, HTTPException
from app.schemas.ProductSchema import Product, CreateProduct, UpdateProduct
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
                "status": StatusCodes.STATUS_CODE_OK,
                "message": "Products found",
                "data": products
            }
        else:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "No products found",
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
                "status": StatusCodes.STATUS_CODE_OK,
                "message": "Product found",
                "data": product
            }
        else:
            response = {
                "status": StatusCodes.STATUS_CODE_BAD_REQUEST,
                "message": "No products found",
                "data": None
            }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/products", response_model=CreateProduct)
async def create_product(product: CreateProduct):
    try:
        product = ProductController().create_product(product)
        response = {
            "status": StatusCodes.STATUS_CODE_CREATED,
            "message": "Product created",
            "data": product
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/products/{product_id}", response_model=UpdateProduct)
async def update_product(product_id: int, product: UpdateProduct):
    try:
        product = ProductController().update_product(product_id, product)
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Product updated",
            "data": product
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/products/{product_id}", response_model=Product)
async def delete_product(product_id: int):
    try:
        product = ProductController().delete_product(product_id)
        response = {
            "status": StatusCodes.STATUS_CODE_OK,
            "message": "Product deleted",
            "data": product
        }
        json_response = jsonable_encoder(response)
        return JSONResponse(content=json_response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
