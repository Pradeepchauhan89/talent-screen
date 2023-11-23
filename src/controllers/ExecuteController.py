import os
import json
from src.schemas.agent import AgentSchema
from src.utils.webhook import call_webhook_with_success, call_webhook_with_error
# import your agent here
# from src.agents.filename import function_name

from src.utils.temp_db import temp_data
from src.core.logger import Logger

logger = Logger()

class ExecuteController:

  def __init__(self):
    self.test = "Agent data"

  def execute(self, payload: AgentSchema):
    try:
      #add_input_here
      resp = ''
      # resp =  callYourAgent()
      #add_output_here
      # Call spritz API
      #add_callback_here

      logger.info('Function execute: Execution complete', resp)
      return { "summary": "Agent execution has been completed.", "detail": resp }
    except Exception as e:
      logger.error('Function execute: error', e)
      raise call_webhook_with_error(str(e), 500)
