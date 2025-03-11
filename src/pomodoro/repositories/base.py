from sqlalchemy.ext.asyncio import AsyncSession


class AbstractSQLRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self):
        await self.session.commit()
