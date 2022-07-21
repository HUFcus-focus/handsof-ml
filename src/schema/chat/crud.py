import enum
from datetime import datetime, timedelta, timezone

from pydantic import BaseModel


class Platforms(str, enum.Enum):
    """
    Supported Platform Class
    """

    ZOOM = "ZOOM"
    SLACK = "SLACK"
    GATHER = "GATHER"
    DISCORD = "DISCORD"


class BaseChatModel(BaseModel):
    """
    Base Chat Model
    """

    message: str | None


class CreateChatModel(BaseChatModel):
    """
    Create Chat Model
    """

    user_id: str
    platform: Platforms
    space: str | None
    channel: str | None
    message: str
    created_at: datetime = datetime.now(tz=timezone(offset=timedelta(hours=9)))

    class Config:
        schema_extra: dict = {"example": {}}


class UpdateChatModel(BaseChatModel):
    """
    Update Chat Model
    """

    message: str
    updated_at: datetime = datetime.now(tz=timezone(offset=timedelta(hours=9)))

    class Config:
        scehma_extra: dict = {"example": {}}
