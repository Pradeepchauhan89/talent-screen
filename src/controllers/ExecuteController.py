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
      payload = payload.dict()
      for param in payload['inputs']:
        # get your input parameter here
        logger.info(param['name'])
        logger.info(param['data'])

      # resp =  callYourAgent()

      # Call spritz TS API
      call_webhook_with_success({
          "status": "completed",
          "data": {
              "title": "Write your title here",
              "info": "Write some information here",
              "output": {
                  "name": "Any suitable name",
                  "type": "list", # check A2A documentation
                  "data": "agent response"
              }
          }
      })
      logger.info('Function execute: Execution complete', "data that you want to log here")
      # logger.info('Function execute: Execution complete', resp)
      return { "summary": "Agent execution has been completed.", "detail": "response that you want to return in api response" }
      # return { "summary": "Agent execution has been completed.", "detail": resp }
    except Exception as e:
      logger.error('Function execute: error', e)
      raise call_webhook_with_error(str(e), 500)
