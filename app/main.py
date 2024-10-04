from fastapi import FastAPI
from app.routers import products, categories, reviews

app = FastAPI(
    title="Product API",
    description="A simple API for Products, Categories, and Reviews",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Product API. Visit /docs for the API documentation."}

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(reviews.router)