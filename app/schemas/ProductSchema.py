from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime


class Product(BaseModel):
    id: int = Field(default=None, primary_key=True)
    name: str
    quantity: int
    price: Decimal
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
