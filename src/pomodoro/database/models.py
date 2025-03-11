from typing import Optional, Annotated

from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


intpk= Annotated[int, mapped_column(primary_key=True, nullable=False)]


class Base(DeclarativeBase):
    pass


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    name: Mapped[str]
    pomodoro_count: Mapped[int]
    category_id: Mapped[int] = mapped_column(nullable=False)


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[intpk]
    type: Mapped[Optional[str]]
    name: Mapped[str]
