import os
import json
import requests
from src.utils.temp_db import temp_data
from src.utils.error_handling import error_handler
from src.core.logger import Logger

logger = Logger()

# This method is responsible to call webhook API:
def call_webhook_with_success(response):
  logger.info("Function call_webhook_with_success method called", response)
  id = temp_data.get('id')
  payload = json.dumps({
      "id": id,
      "status": response.get("status"),
      "data": response.get("data")
  })
  webhookUrl = os.environ.get('WEB_HOOK_URL')
  resp = requests.post(webhookUrl, data=payload)
  return resp


# This method is responsible for handle error and call webhook:
def call_webhook_with_error(error, code: int):
  logger.info("Function call_webhook_with_error method called", error)
  response = {"status": "failed", "data": {"reason": error}}
  call_webhook_with_success(response)
  raise error_handler(error, code)
