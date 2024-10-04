from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    price: float
    category: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True