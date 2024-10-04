# app/routers/categories.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.category import Category
from app.services.category_service import CategoryService

router = APIRouter()

@router.get("/categories/", response_model=List[Category])
def get_categories():
    return CategoryService.get_all_categories()

@router.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int):
    category = CategoryService.get_category_by_id(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category