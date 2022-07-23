from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/slack/{team_id}")
async def send_to_slack(request: Request):
    """ """
    try:

        return

    except Exception as error:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": str(error)},
        )
