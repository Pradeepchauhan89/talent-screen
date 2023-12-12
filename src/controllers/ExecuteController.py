import os
import json

import io
import chardet
from docx import Document
from PyPDF2 import PdfReader
from google.oauth2 import service_account
from googleapiclient.discovery import build

from src.schemas.agent import AgentSchema
from src.utils.webhook import call_webhook_with_success, call_webhook_with_error
from urllib.parse import urlparse
# import your agent here
from src.agents.get_files import file_list
from src.agents.get_file_contents import file_content
from src.agents.screen import screen_resume

from src.utils.temp_db import temp_data
from src.core.logger import Logger

logger = Logger()

class ExecuteController:

  def __init__(self):
    self.test = "Agent data"

  def execute(self, payload: AgentSchema):
    try:

      resp={}
      files = []
      payload = payload.dict()
      for param in payload["inputs"]:
  
        url = ''
        if param['name'] == "url":
          url = param['data']
        
        folder_id = extract_folder_id_from_url(url)
        files = file_list(folder_id)

        files = files.get('files', [])
      
      call_webhook_with_success({
        "status": "Inprogress",
        "data": {
          "title": "Fetching files...",
          "info": "Agent is fetching file from drive.",
        }
      })
      
      for file in files:
        print(f"\n\n\n\n\n{file['name']} ({file['id']})")
        file_id = file['id']
        call_webhook_with_success({
          "status": "Inprogress",
          "data": {
            "title": f"Fetching file content {file['name']}",
            "info": "Agent is fetching file from drive.",
          }
        })
        file_text = file_content(file)
        screen_resume(file_text)

      call_webhook_with_success({
        "status": "completed",
        "data": {
          "title": "Agent executed successfully.",
          "info": "All resume has been reviewed. Please visit Doc url.",
          "output": {
            "name": "Doc Url",
            "type": "url",
            "data": "Greeting of the day :pray::pray:"
          }
        }
      })

      logger.info('Function execute: Execution complete', resp)
      return { "summary": "Agent execution has been completed.", "detail": resp }
    except Exception as e:
      # logger.error('Function execute: error', e)
      print('error====')
      print(e)
      raise call_webhook_with_error(str(e), 500)


def extract_folder_id_from_url(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    if 'folders' in path_parts:
        folder_index = path_parts.index('folders')
        if folder_index + 1 < len(path_parts):
            folder_id = path_parts[folder_index + 1]
            return folder_id

    return None
