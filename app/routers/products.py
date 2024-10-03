# app/routers/products.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product
from app.data.sample_data import products

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[Product])
def get_products():
    return products

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
