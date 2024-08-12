from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field

from core.dto.mixins import CategoryProductsMixinDTO
from core.dto.product import SimpleProduct


class SimpleCategory(CategoryProductsMixinDTO):
    parent_id: Optional[UUID] = None


class CreateCategory(BaseModel):
    parent_id: Optional[UUID]
    name: str = Field(..., max_length=100)


class CategoryWithProductsDTO(SimpleCategory):
    products: Optional[list[Optional['SimpleProduct']]]
