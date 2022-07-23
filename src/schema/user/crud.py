from pydantic import BaseModel, EmailStr


class BaseUserModel(BaseModel):
    """
    Base User Model
    """

    pass


class CreateUserModel(BaseUserModel):
    """
    Create User Model
    """

    name: str
    email: EmailStr
    password: str


class UpdateUserModel(BaseUserModel):
    """
    Update User Model
    """

    pass


class SlackIntegrationModel(BaseUserModel):
    """
    Slack Integration Model
    """

    slack: dict[str, str]
