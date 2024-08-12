from datetime import datetime
from uuid import UUID

from sqlalchemy import Uuid, text, String, Boolean, Integer, Float, ForeignKey, event, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from utils import unique_slug_generator
from .base import Base
from .mixins import TimeStampMixin


class Product(Base, TimeStampMixin):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, server_default=text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    image_url: Mapped[str] = mapped_column(String, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    rating: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    category_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category: Mapped['Category'] = relationship(back_populates="products")


def generate_slug(mapper, connection, target):
    session = Session(bind=connection)
    target.slug = unique_slug_generator(session, target, 'name')


event.listen(Product, 'before_insert', generate_slug)
event.listen(Product, 'before_update', generate_slug)