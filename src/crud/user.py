from bson.objectid import ObjectId
from fastapi import Request

from src.crud.base import CRUDBase
from src.schema import CreateUserModel, SlackIntegrationModel, UpdateUserModel


class CRUDUser(CRUDBase[CreateUserModel, UpdateUserModel]):
    async def platform_integrate(
        self,
        request: Request,
        user_id: str,
        update_data: SlackIntegrationModel,
    ):
        """
        Slack Integration

        To-do
        1. Create and raise AlreadyExistsException
        """

        session = request.app.db[self.collection]

        tokens = await session.find_one(
            {"_id": ObjectId(user_id)},
            {"projection": {"_id": False, "slack.accessToken": True}},
        )
        converted_update_data = update_data.dict()
        for token in tokens:
            if token == converted_update_data["slack"]["accessToken"]:
                raise Exception("Alrey Exists")

        result = await session.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": update_data},
        )

        return result


user_crud = CRUDUser(collection="user")
