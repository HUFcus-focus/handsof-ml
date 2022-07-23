from bson.objectid import ObjectId
from fastapi import Request
from fastapi.encoders import jsonable_encoder

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
        platform: Platforms,
        update_data: SlackIntegrationModel,
    ):
        session = request.app.db[self.collection]

        result = await session.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {platform: jsonable_encoder(**update_data)}},
        )
        print(result.__dict__)
        return result


user_crud = CRUDUser(collection="user")
