from typing import TypeVar, Generic, Type, Any, Optional, Sequence

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Query

from repository.interfaces.base import AbstractRepository
from repository.models import Base

SQLAlchemyModelType = TypeVar('SQLAlchemyModelType', bound=Base, covariant=True)
DTOModel = TypeVar('DTOModel', bound=BaseModel, covariant=True)


class SQLAlchemyRepository(AbstractRepository, Generic[DTOModel]):
    model: Type[SQLAlchemyModelType]
    dto_model: Type[DTOModel]
    lookup_field = 'id'

    def __init__(self, session: AsyncSession):
        self._session = session

    async def retrieve(self, lookup_value: Any) -> DTOModel:
        lookup_field = getattr(self.model, self.lookup_field)
        if lookup_field is None:
            raise ValueError("Model does not have a lookup field")
        query = select(self.model).where(lookup_field == lookup_value)
        result = await self._session.execute(query)
        instance: SQLAlchemyModelType | None = result.scalars().first()
        if instance is None:
            raise NoResultFound(f"Instance with {lookup_field} == {lookup_value} not found")
        return self.dto_model.model_validate(instance, from_attributes=True)

    async def create(self, model_data: BaseModel) -> DTOModel:
        new_model = self.model(**model_data.model_dump())
        self._session.add(new_model)
        await self._session.commit()
        await self._session.refresh(new_model)
        return self.dto_model.model_validate(new_model, from_attributes=True)

    async def update(self, lookup_value, update_data: BaseModel) -> DTOModel:
        obj = await self.retrieve(lookup_value)
        update_dict = update_data.model_dump()
        for key, value in update_dict.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
            else:
                raise AttributeError(f"Model does not have attribute {key}")
        await self._session.commit()
        return self.dto_model.model_validate(obj, from_attributes=True)

    async def destroy(self, lookup_value) -> None:
        obj = await self.retrieve(lookup_value)
        await self._session.delete(obj)
        await self._session.commit()

    async def list(self, filter_query: Optional[Query] = None) -> list[DTOModel]:
        if filter_query is None:
            result = await self._session.execute(select(self.model))
        else:
            result = await self._session.execute(filter_query)
        return [self.dto_model.model_validate(obj, from_attributes=True)
                for obj in result.scalars().all()]
