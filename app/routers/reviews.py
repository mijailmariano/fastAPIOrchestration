# app/routers/reviews.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.review import Review
from app.data.sample_data import reviews

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get("/", response_model=List[Review])
def get_reviews():
    return reviews

@router.get("/{review_id}", response_model=Review)
def get_review(review_id: int):
    for review in reviews:
        if review.id == review_id:
            return review
    raise HTTPException(status_code=404, detail="Review not found")

