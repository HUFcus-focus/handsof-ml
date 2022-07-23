from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from src.util import slack

router = APIRouter()


@router.get("/slack")
async def slack_oauth(
    code: str = Query(default=None, description="Slack에서 제공해주는 인증을 위한 임시 코드")
) -> None:
    """
    Slack OAuth 2.0 Integration
    """
    try:
        worker = slack.Worker()
        result = worker.oauth_access(auth_code=code)

        if result["status"]:
            print(result["detail"])

        else:
            JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail": result["detail"]},
            )

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(error)},
        )
