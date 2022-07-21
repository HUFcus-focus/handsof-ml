from typing import Generic, TypeVar

from pydantic import BaseModel

CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class CRUDBase(Generic[CreateSchema, UpdateSchema]):
    """
    Base CRUD Class
    """

    def __init__(self, collection) -> None:
        self.collection = collection

    async def get(self):
        """ """
        pass

    async def get_multi(self):
        """ """
        pass

    async def create(self):
        """ """
        pass

    async def update(self):
        """ """
        pass

    async def delete(self):
        """ """
        pass
