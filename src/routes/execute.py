from fastapi import APIRouter
from src.controllers.ExecuteController import ExecuteController
from src.schemas.agent import ApiResponse, AgentSchema
from src.utils.temp_db import temp_data
from dotenv import load_dotenv

load_dotenv()

# prefix="/execute",
router = APIRouter(tags=['Agent execution'])


@router.post('/execute', response_model=ApiResponse)
def execute_agent(request: AgentSchema):
  
  # save request id in temp_data
  temp_data['id'] = request.id
  temp_data['isExecutionContinue'] = True
  return ExecuteController().execute(request)
