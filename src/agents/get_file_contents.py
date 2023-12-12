import os
from io import BytesIO
import chardet
from docx import Document
from PyPDF2 import PdfReader
from google.oauth2 import service_account
from googleapiclient.discovery import build
import openai
import fitz 

from docx import Document

openai.api_key = os.environ.get('OPEN_API_KEY')

def file_content(file):
  try:
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_directory, '..', 'static/credentials.json')
    credentials = service_account.Credentials.from_service_account_file(
      json_file_path, scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=credentials)
    text_content = ''
    if file['name'].endswith('.docx'):
        file_content = get_file_content(service, file['id'])
        text_content = read_docx_content(file_content)
    elif file['name'].endswith('.pdf'):
        file_content = get_file_content(service, file['id'])
        text_content = read_pdf_content(file_content)
    else:
      print(f"\n\n\ unsupported file format {file['name']} \n\n")
  except Exception as e:
      print(f"\n\n\ got error: get content for file {file['name']} - {str(e)} \n\n")

  return text_content

def get_file_content(service, file_id):
  try:
    file_content = ""
    if file_content != "":
      request = service.files().get_media(fileId=file_id)
      file_content = BytesIO(request.execute())
  except Exception as e:
    print(f"\n\n\ get_file_content: get file content for file {file_id} - {str(e)} \n\n")

  return file_content

def read_docx_content(file_content):
    try:
      text_content = ""
      if file_content != "":
        doc = Document(file_content)
        text_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
      print(f"\n\n\ read_docx_content: get doc content for file {str(e)} \n\n")

    return text_content

def read_pdf_content(file_content):
    try:
      text_content = ""
      if file_content != "":
        pdf_document = fitz.open(stream=file_content.read())
        text_content = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document[page_number]
            text_content += page.get_text()
    except Exception as e:
      print(f"\n\n\ read_pdf_content: get pdf content for file {str(e)} \n\n")

    return text_content