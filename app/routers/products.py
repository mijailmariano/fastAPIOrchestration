from fastapi import APIRouter, HTTPException
from typing import List
from app.models.product import Product, ProductCreate
from app.services.product_service import ProductService

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", response_model=List[Product])
def get_products():
    return ProductService.get_all_products()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    product = ProductService.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    return ProductService.create_product(product)