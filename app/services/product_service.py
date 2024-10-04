from typing import List
from app.models.product import Product, ProductCreate
from app.data.sample_data import products

class ProductService:
    @staticmethod
    def get_all_products() -> List[Product]:
        return products

    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return next((p for p in products if p.id == product_id), None)

    @staticmethod
    def create_product(product: ProductCreate) -> Product:
        new_id = max(p.id for p in products) + 1
        new_product = Product(id=new_id, **product.dict())
        products.append(new_product)
        return new_product