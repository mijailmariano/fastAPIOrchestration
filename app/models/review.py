# app/models/review.py
from pydantic import BaseModel

class Review(BaseModel):
    id: int
    product_id: int
    rating: int
    comment: str