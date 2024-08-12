from uuid import UUID

from sqlalchemy import select

from core.dto.category import SimpleCategory
from repository.interfaces.sqlalchemy_repository import SQLAlchemyRepository
from repository.models import Category


class CategoryRepository(SQLAlchemyRepository[SimpleCategory]):
    model = Category
    dto_model = SimpleCategory
    lookup_field = 'slug'

    async def get_subcategories(self, parent_id: UUID):
        query = select(self.model).where(self.model.parent_id == parent_id)
        return await self.list(filter_query=query)

