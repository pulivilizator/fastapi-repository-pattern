from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from core.services.product_service import ProductService
from repository.implementations.product_repository import ProductRepository
from .dependencies import get_session


async def get_product_service(session: Annotated[AsyncSession, Depends(get_session)]) -> ProductService:
    repository = ProductRepository(session)
    return ProductService(repository)
