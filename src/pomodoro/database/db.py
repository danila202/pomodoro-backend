from sqlalchemy.ext.asyncio import ( # type: ignore[import]
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from src.pomodoro.database.models import Base
from src.pomodoro.settings import settings


async def create_tables(engine: AsyncEngine) -> None:
    print("Create tables")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


engine: AsyncEngine = create_async_engine(url=settings.db_uri, pool_size=15, max_overflow=10)

async_session_maker = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def create_session():
    async with async_session_maker() as session:
        yield session


