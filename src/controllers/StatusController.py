from src.schemas.status import StatusSchema
from src.utils.temp_db import temp_data


class StatusController:

  def __init__(self):
    self.test = "test data"

  @classmethod
  def get_status(self, request_id: StatusSchema):
    agent_id = temp_data.get('id')
    doc = {}
    doc['id'] = request_id
    if agent_id is not None and request_id == agent_id:
      doc['id'] = agent_id
      doc['status'] = temp_data.get('status')
      doc['data'] = temp_data.get('data')
    else:
      doc['status'] = "not_found"
      doc['data'] = {
        "info":
        "The specified task is not recognized or found in our system. It may have been cleared due to a system restart, expired, or never existed."
      }

    return doc
