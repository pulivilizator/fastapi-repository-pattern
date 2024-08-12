from uuid import UUID

from pydantic import BaseModel, Field


class CategoryProductsMixinDTO(BaseModel):
    id: UUID
    name: str = Field(..., max_length=100)
    slug: str = Field(..., max_length=100)
    is_active: bool


