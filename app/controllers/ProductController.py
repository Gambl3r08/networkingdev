from sqlmodel import select
from app.core.db import get_session
from app.models.ProductModel import Product


class ProductController:

    def __init__(self):
        self.db = get_session()
        self.ProductModel = Product

    def create_product(self, product: Product):
        product_data = Product.model_validate(product)
        self.db.add(product_data)
        self.db.commit()
        self.db.refresh(product_data)
        return product_data

    def read_product(self, product_id: int):
        product = self.db.get(Product, product_id)
        return product

    def read_products(self):
        products = self.db.exec(select(Product)).all()
        return products

    def update_product(self, product_id: int, product: Product):
        product_data = self.db.get(Product, product_id)
        product_data.name = product.name
        product_data.quantity = product.quantity
        product_data.price = product.price
        self.db.add(product_data)
        self.db.commit()
        self.db.refresh(product_data)
        return product_data

    def delete_product(self, product_id: int):
        product = self.db.get(Product, product_id)
        self.db.delete(product)
        self.db.commit()
        return product
