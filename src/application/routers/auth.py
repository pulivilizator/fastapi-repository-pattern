from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, status
from passlib.context import CryptContext

from core import dto
from application.dependencies.auth_dependencies import get_auth_service
from core.services.auth_service import AuthService

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=dto.UserId)
async def create_user(create_user_data: Annotated[dto.UserCreate, Body()],
                      auth_service: Annotated[AuthService, Depends(get_auth_service)]):
    user_id = await auth_service.create(create_user_data)
    return dto.UserId(user_id=user_id)
