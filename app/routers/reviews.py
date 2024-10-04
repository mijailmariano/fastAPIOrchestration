# app/routers/reviews.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.review import Review
from app.services.review_service import ReviewService

router = APIRouter()

@router.get("/reviews/", response_model=List[Review])
def get_reviews():
    return ReviewService.get_all_reviews()

@router.get("/reviews/{review_id}", response_model=Review)
def get_review(review_id: int):
    review = ReviewService.get_review_by_id(review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.get("/products/{product_id}/reviews/", response_model=List[Review])
def get_product_reviews(product_id: int):
    reviews = ReviewService.get_reviews_by_product_id(product_id)
    if not reviews:
        raise HTTPException(status_code=404, detail="No reviews found for this product")
    return reviews