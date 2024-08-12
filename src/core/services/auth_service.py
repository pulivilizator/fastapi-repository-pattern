from typing import Any
from uuid import UUID
import re

from passlib.context import CryptContext

from .base import BaseService
from repository import AuthRepository
from core import dto

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class AuthService(BaseService[dto.UserInDB]):
    repository: AuthRepository

    async def create(self, data: dto.UserCreate) -> UUID:
        dict_data = data.model_dump()
        password = dict_data.pop('password')
        self._validate_password(password)
        hashed_password = bcrypt_context.hash(password)
        dict_data['password_hash'] = hashed_password
        data_with_hashed_password = dto.UserInDB.model_validate(dict_data, from_attributes=True)
        return await self.repository.create(data_with_hashed_password)

    def _validate_password(self, password):
        r_p = re.compile('^(?=\S{8,40}$)(?=.*?\d)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[^A-Za-z\s0-9])')
        if r_p.match(password):
            return True

        raise ValueError('Invalid password')
