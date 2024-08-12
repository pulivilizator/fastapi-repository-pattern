from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.db import Sessionmaker


async def get_session() -> AsyncSession:
    async with Sessionmaker() as session:
        yield session
