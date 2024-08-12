from typing import Optional
from uuid import UUID

from pydantic import HttpUrl

from core.dto.mixins import CategoryProductsMixinDTO


class SimpleProduct(CategoryProductsMixinDTO):
    description: Optional[str] = None
    price: int
    image_url: HttpUrl
    stock: int = 0
    rating: float = 0.0
    category_id: UUID


class ProductWithCategory(SimpleProduct):
    category: Optional['SimpleCategory']
