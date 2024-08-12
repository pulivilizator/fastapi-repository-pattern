from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def retrieve(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def destroy(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def list(self, *args, **kwargs):
        raise NotImplementedError


