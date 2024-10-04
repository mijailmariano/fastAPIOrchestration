# app/services/review_service.py
from typing import List
from app.models.review import Review
from app.data.sample_data import reviews

class ReviewService:
    @staticmethod
    def get_all_reviews() -> List[Review]:
        return reviews

    @staticmethod
    def get_review_by_id(review_id: int) -> Review:
        return next((r for r in reviews if r.id == review_id), None)

    @staticmethod
    def get_reviews_by_product_id(product_id: int) -> List[Review]:
        return [r for r in reviews if r.product_id == product_id]