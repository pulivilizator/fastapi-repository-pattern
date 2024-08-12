from uuid import UUID

from sqlalchemy import Uuid, text, String, Boolean, ForeignKey, event
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session

from .base import Base
from .mixins import TimeStampMixin
from utils import unique_slug_generator


class Category(Base, TimeStampMixin):
    __tablename__ = "categories"

    id: Mapped[UUID] = mapped_column(Uuid,
                                     primary_key=True,
                                     server_default=text('gen_random_uuid()'))
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    parent_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey('categories.id', ondelete='CASCADE'), nullable=True)

    products: Mapped[list['Product']] = relationship(back_populates='category')


def generate_slug(mapper, connection, target):
    session = Session(bind=connection)
    target.slug = unique_slug_generator(session, target, 'name')


event.listen(Category, 'before_insert', generate_slug)
event.listen(Category, 'before_update', generate_slug)
