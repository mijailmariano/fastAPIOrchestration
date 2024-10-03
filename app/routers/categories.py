# app/routers/categories.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.category import Category
from app.data.sample_data import categories

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("/", response_model=List[Category])
def get_categories():
    return categories

@router.get("/{category_id}", response_model=Category)
def get_category(category_id: int):
    for category in categories:
        if category.id == category_id:
            return category
    raise HTTPException(status_code=404, detail="Category not found")
