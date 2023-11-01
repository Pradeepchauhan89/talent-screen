from src.utils.temp_db import temp_data
from src.utils.error_handling import error_handler
from src.core.logger import Logger

logger = Logger()

class AbortController:

  def __init__(self):
    self.test = "test data"

  # This method is abort a execution
  @classmethod
  def execution_abort(self):
    try:
      logger.info("Function execution_abort method called")
      temp_data['isExecutionContinue'] = False
      return {"data": "", "detail": ""}
    except Exception as e:
      logger.error('Function execution_abort: error', e)
      raise error_handler(e, 500)
