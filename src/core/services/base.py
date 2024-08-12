from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

from pydantic import BaseModel

from repository import AbstractRepository


class AbstractService(ABC):
    @abstractmethod
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    @abstractmethod
    async def get_one(self, lookup_value: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @abstractmethod
    async def create(self, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def update(self, lookup_value: Any, data: Any) -> Any:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, lookup_value: Any) -> Any:
        raise NotImplementedError


DTOModel = TypeVar('DTOModel', bound=BaseModel, covariant=True)


class BaseService(AbstractService, Generic[DTOModel]):
    def __init__(self, repository: AbstractRepository):
        self.repository = repository

    async def get_one(self, lookup_value: Any) -> DTOModel:
        return await self.repository.retrieve(lookup_value)

    async def get_all(self) -> list[DTOModel]:
        return await self.repository.list()

    async def create(self, data: Any) -> DTOModel:
        return await self.repository.create(data)

    async def update(self, lookup_value: Any, data: Any) -> DTOModel:
        return await self.repository.update(lookup_value, data)

    async def delete(self, lookup_value: Any) -> Any:
        return await self.repository.destroy(lookup_value)
