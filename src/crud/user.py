from fastapi import Request
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient

from src.crud.base import CRUDBase
from src.schema import (
    CreateUserModel,
    Platforms,
    SlackIntegrationModel,
    UpdateUserModel,
)


class CRUDUser(CRUDBase[CreateUserModel, UpdateUserModel]):
    async def platform_integrate(
        self,
        request: Request,
        user_id: str,
        platform: Platforms.value,
        update_data: SlackIntegrationModel,
    ):
        session: AsyncIOMotorClient = request.app.db[self.collection]

        result = await session.update(
            {"_id": user_id},
            {"$push": {platform: jsonable_encoder(update_data)}},
        )

        return result


user_crud = CRUDUser(collection="user")
