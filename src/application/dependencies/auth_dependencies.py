from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends

from core.services.auth_service import AuthService
from repository import AuthRepository
from .dependencies import get_session


async def get_auth_service(session: Annotated[AsyncSession, Depends(get_session)]) -> AuthService:
    repository = AuthRepository(session)
    return AuthService(repository)