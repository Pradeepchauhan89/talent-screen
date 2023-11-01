import validators
from fastapi import APIRouter, Request
from src.schemas.agent import ApiResponse
from src.controllers.AbortController import AbortController

# prefix="/abort",
router = APIRouter(tags=['Process Abort'])


@router.get('/abort', response_model=ApiResponse)
def abort_execution():
  return AbortController.execution_abort()
