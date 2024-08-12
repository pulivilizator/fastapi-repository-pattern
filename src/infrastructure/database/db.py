from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings

engine = create_async_engine(url=settings.get('database').get('dsn'), echo=True)

Sessionmaker = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=True)