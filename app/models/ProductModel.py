from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, DateTime, text
from datetime import datetime, timezone


class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    quantity: int
    price: float
    active: int = Field(
        default=1, sa_column=Column(
            Integer, nullable=False, server_default=text('1')))
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column=Column(
            DateTime, default=datetime.now(timezone.utc)))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column=Column(
            DateTime, default=datetime.now(
                timezone.utc), onupdate=datetime.now(timezone.utc)))
