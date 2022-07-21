from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/slack")
async def slack_oauth(request: Request):
    print(request.__dict__)
