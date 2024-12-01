import uuid

from typing import List
from enum import Enum as PyEnum
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, DateTime, Boolean, Float, Enum, func

from src.database.crud import BaseCRUD


class TransactionType(PyEnum):
    INCOME = "приход"
    EXPENSE = "расход"


class User(BaseCRUD):

    __tablename__ = "user_account"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(254), unique=True, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now().replace(tzinfo=None), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_login: Mapped[DateTime] = mapped_column(DateTime, nullable=True)

    transactions: Mapped[List['Transaction']] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )
    budgets: Mapped[List["Budget"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email
        }

    def __str__(self):
        return f"<User(id={self.id}, name={self.name}, email={self.email}, is_active={self.is_active})>"


class Category(BaseCRUD):
    __tablename__ = 'category'

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    type: Mapped[TransactionType] = mapped_column(Enum(TransactionType), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now().replace(tzinfo=None), nullable=False)

    transactions: Mapped[List["Transaction"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )
    budgets: Mapped[List["Budget"]] = relationship(
        back_populates="category", cascade="all, delete-orphan"
    )

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "type": self.type.value
        }


    def __str__(self):
        return f"<Category(id={self.id}, name={self.name}, type={self.type})>"


class Transaction(BaseCRUD):
    __tablename__ = "transaction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user_account.id"))
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("category.id"))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=lambda: datetime.now().replace(tzinfo=None), nullable=False)
    short_description: Mapped[str] = mapped_column(String(256), nullable=True)

    user: Mapped['User'] = relationship(back_populates='transactions')
    category: Mapped['Category'] = relationship("Category", back_populates='transactions', lazy='select')

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "category_id": str(self.category_id),
            "category_name": self.category.name,
            "amount": self.amount,
            'short_description': self.short_description
        }

    def __str__(self):
        return f"<Transaction(id={self.id}, amount={self.amount}, category={self.category}, description={self.short_description}, added={self.category})>"

    @classmethod
    async def get_statistic(cls, asession: AsyncSession, start_date, end_date):
        statistic = await asession.execute(cls).filter(
            cls.created_at >= start_date,
            cls.created_at <= end_date
        ).all()

        return statistic


class Budget(BaseCRUD):
    __tablename__ = "budget"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user_account.id"))
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("category.id"))
    amount: Mapped[float] = mapped_column(Float, nullable=False)
    start_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)

    user: Mapped['User'] = relationship(back_populates='budgets')
    category: Mapped['Category'] = relationship(back_populates='budgets')

    def __str__(self):
        return f"<Budget(id={self.id}, user_id={self.user_id}, category_id={self.category_id}, amount={self.amount})>"