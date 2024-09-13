from sqlmodel import Session, select

from database.models import Product


def create_product(product: Product, db: Session):
    product_data = Product.model_validate(product)
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return product_data

def read_product(product_id: int, db: Session):
    product = db.get(Product, product_id)
    return product

def read_products(db: Session):
    products = db.exec(select(Product)).all()
    return products

def update_product(product_id: int, product: Product, db: Session):
    product_data = db.get(Product, product_id)
    product_data.name = product.name
    product_data.quantity = product.quantity
    product_data.price = product.price
    db.add(product_data)
    db.commit()
    db.refresh(product_data)
    return product_data

def delete_product(product_id: int, db: Session):
    product = db.get(Product, product_id)
    db.delete(product)
    db.commit()
    return product
