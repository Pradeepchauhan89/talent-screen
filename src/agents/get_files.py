import os
import io
import chardet
from docx import Document
from PyPDF2 import PdfReader
from google.oauth2 import service_account
from googleapiclient.discovery import build
import openai

openai.api_key = os.environ.get('OPEN_API_KEY')

def file_list(folder_id):
  script_directory = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(script_directory, '..', 'static/credentials.json')
  credentials = service_account.Credentials.from_service_account_file(
    json_file_path, scopes=['https://www.googleapis.com/auth/drive'])
  drive_service = build('drive', 'v3', credentials=credentials)

  # List files in the folder.
  results = drive_service.files().list(q=f"'{folder_id}' in parents", pageSize=1000, fields="files(id, name)").execute()
  return results