# app/services/category_service.py
from typing import List
from app.models.category import Category
from app.data.sample_data import categories

class CategoryService:
    @staticmethod
    def get_all_categories() -> List[Category]:
        return categories

    @staticmethod
    def get_category_by_id(category_id: int) -> Category:
        return next((c for c in categories if c.id == category_id), None)