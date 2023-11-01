import os
import json

from src.core.logger import Logger

logger = Logger()

class DiscoverController:

  def __init__(self):
    self.test = "test data"

  @classmethod
  def documentation(self):
    doc = {}
    current_directory = os.path.dirname(__file__)
    file_path = os.path.normpath(
        os.path.join(current_directory, '../static/agent.json'))

    with open(file_path, "r") as json_file:
      doc = json.load(json_file)
      doc['url'] = os.environ.get('APP_URL')
      doc['name'] = os.environ.get('AGENT_DISPLAY_NAME')
      doc['color'] = os.environ.get('AGENT_COLOR')

    return doc