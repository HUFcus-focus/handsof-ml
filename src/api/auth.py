from fastapi import APIRouter, Query, Request

from src.util import slack

router = APIRouter()


@router.post("/slack")
async def slack_oauth(
    request: Request,
    code: str = Query(..., description="Slack에서 제공해주는 인증을 위한 임시 코드"),
):
    worker = slack.Worker()
    result = worker.oauth_access(auth_code=code)
    print(result)
