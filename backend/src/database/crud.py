from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase


class BaseCRUD(DeclarativeBase):

    @classmethod
    async def add(cls, session: AsyncSession, data):
        new = cls(**data.model_dump())

        session.add(new)
        await session.commit()

        if cls.__name__ == "Transaction":
            await session.refresh(new, attribute_names=["category"])

        return new.to_dict()

    @classmethod
    async def get(cls, id, session: AsyncSession):
        res = await session.get(cls, id)
        return res.to_dict() if res else None

    @classmethod
    async def get_all(cls, session: AsyncSession):
        stmt = select(cls)
        result = await session.execute(stmt)
        res_all = result.scalars().all()
        return [res.to_dict() for res in res_all] if res_all else None

    @classmethod
    async def remove(cls, id, session: AsyncSession):
        obj = await session.get(cls, id)
        if obj:
            await session.delete(obj)
            await session.commit()
            return True
        return False

    async def update(self):
        pass


