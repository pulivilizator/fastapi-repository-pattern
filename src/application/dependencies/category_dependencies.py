from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from core.services.category_service import CategoryService
from repository import CategoryRepository
from .dependencies import get_session


async def get_category_service(session: Annotated[AsyncSession, Depends(get_session)]) -> CategoryService:
    repository = CategoryRepository(session)
    return CategoryService(repository)