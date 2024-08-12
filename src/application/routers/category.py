from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, Path, Body, Query

from application.dependencies.category_dependencies import get_category_service
from core import dto
from core.services.category_service import CategoryService

router = APIRouter(prefix='/categories', tags=['category'])


@router.get('/',
            response_model=list[dto.SimpleCategory])
async def get_categories(category_service: Annotated[CategoryService, Depends(get_category_service)]):
    return await category_service.get_all()


@router.get('/subcategories/',
            response_model=list[dto.SimpleCategory])
async def get_subcategories(category_service: Annotated[CategoryService, Depends(get_category_service)],
                            parent_id: Annotated[UUID, Query(title='Parent category ID')]):
    return await category_service.get_subcategories(parent_id)


@router.get('/{slug}/',
            response_model=dto.SimpleCategory)
async def get_category(category_service: Annotated[CategoryService, Depends(get_category_service)],
                       slug: Annotated[str, Path(title='Category slug', max_length=100)]):
    return await category_service.get_one(slug)


@router.post('/',
             response_model=dto.SimpleCategory,
             response_model_exclude_none=True)
async def create_category(category_service: Annotated[CategoryService, Depends(get_category_service)],
                          category_data: Annotated[dto.CreateCategory, Body()]):
    create_data = dto.CreateCategory.model_validate(category_data, from_attributes=True)
    return await category_service.create(create_data)
