from typing import Generic, TypeVar

from pydantic import BaseModel  # type: ignore[import]


T = TypeVar("T")


class ListModel(BaseModel, Generic[T]):
    data: list[T]