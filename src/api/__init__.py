from fastapi import APIRouter

from src.api import auth

router = APIRouter()

router.include_router(router=auth.router, prefix="/auth", tags=["인증"])
