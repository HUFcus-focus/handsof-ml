from src.crud.base import CRUDBase
from src.schema import CreateSlackChattingLogModel, UpdateSlackChattingLogModel


class CRUDSlack(
    CRUDBase[CreateSlackChattingLogModel, UpdateSlackChattingLogModel]
):
    pass
