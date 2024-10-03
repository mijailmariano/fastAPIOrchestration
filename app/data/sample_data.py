# app/data/sample_data.py
from app.models.product import Product
from app.models.category import Category
from app.models.review import Review

products = [
    Product(id=1, name="Product A", price=10.99, category="Category 1"),
    Product(id=2, name="Product B", price=12.99, category="Category 2"),
    Product(id=3, name="Product C", price=8.99, category="Category 1")
]

categories = [
    Category(id=1, name="Category 1", description="Category description 1"),
    Category(id=2, name="Category 2", description="Category description 2")
]

reviews = [
    Review(id=1, product_id=1, rating=5, comment="Great product!"),
    Review(id=2, product_id=2, rating=4, comment="Good value"),
    Review(id=3, product_id=1, rating=3, comment="Average quality")
]