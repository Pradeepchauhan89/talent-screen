from pydantic import BaseModel
from typing import List, Optional, Any

class InputItem(BaseModel):
    name: str
    type: str
    data: str

class AgentSchema(BaseModel):
    id: str
    inputs: List[InputItem]

class ApiResponse(BaseModel):
  data: Optional[Any] = None
  detail: Optional[Any] = None
