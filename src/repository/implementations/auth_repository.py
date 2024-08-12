from uuid import UUID

from core import dto
from repository.interfaces.sqlalchemy_repository import SQLAlchemyRepository
from repository.models import User


class AuthRepository(SQLAlchemyRepository[dto.UserInDB]):
    model = User
    dto_model = dto.UserInDB

    async def create(self, model_data: dto.UserInDB) -> UUID:
        new_user = self.model(**model_data.model_dump())
        self._session.add(new_user)
        await self._session.commit()
        return new_user.id
