from uuid import UUID

from .base import BaseService
from ..dto.category import SimpleCategory
from repository.implementations.category_repository import CategoryRepository


class CategoryService(BaseService[SimpleCategory]):
    repository: CategoryRepository
    async def get_subcategories(self, parent_id: UUID) -> list[SimpleCategory]:
        return await self.repository.get_subcategories(parent_id)
