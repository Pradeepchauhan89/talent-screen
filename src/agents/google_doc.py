import os
import io
from google.oauth2 import service_account
from googleapiclient.discovery import build
import json
import time
from googleapiclient.errors import HttpError
from google.oauth2.service_account import Credentials

def create_doc(title):
  script_directory = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(script_directory, '..',
                                'static/credentials.json')
  credentials = service_account.Credentials.from_service_account_file(
      json_file_path, scopes=['https://www.googleapis.com/auth/drive'])
  scopes = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
  ]
  # Load the credentials and create a service
  drive_service = build('drive',
                        'v3',
                        credentials=credentials,
                        static_discovery=False)
  docs_service = build('docs',
                       'v1',
                       credentials=credentials,
                       static_discovery=False)
  body = {'title': title}
  doc = docs_service.documents().create(body=body).execute()
  doc_id = doc.get('documentId')
  # Try to make the document public
  try:
    drive_service.permissions().create(
      fileId=doc_id,
      body={
        'type': 'anyone',
        'role': 'writer',  # Changed from 'reader' to 'writer'
      },
      fields='id',
    ).execute()
  except HttpError as error:
    print(f'An error occurred: {error}')
  doc_url = f'https://docs.google.com/document/d/{doc_id}/'
  print(f'Created a new document with title: {title}.')
  print(f'Google Docs URL: {doc_url}')
  return doc_id

# Define functions to add title and text to google docs
def add_title_to_doc(document_id,
                     title,
                     start_index,
                     named_style='HEADING_2',
                     new_line=0):
  
  # Define the specific styles for each named heading
  heading_styles = {
    'HEADING_1': {
      'font': 'Nunito',
      'bold': True,
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.545
      },
      'size': 20
    },
    'HEADING_2': {
      'font': 'Nunito',
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.0
      },
      'size': 12
    },
    'HEADING_3': {
      'font': 'Nunito',
      'bold': True,
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.0
      },
      'size': 16
    },
    'HEADING_4': {
      'font': 'Nunito',
      'bold': True,
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.0
      },
      'size': 14
    },
    'HEADING_5': {
      'font': 'Nunito',
      'bold': True,
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.0
      },
      'size': 12
    },
    'HEADING_6': {
      'font': 'Nunito',
      'bold': True,
      'color': {
        'red': 0.0,
        'green': 0.0,
        'blue': 0.0
      },
      'size': 11
    },
  }
  # Get the specific style for the given named style
  style = heading_styles.get(named_style, heading_styles['HEADING_2'])
  # Load the credentials and create a service
  script_directory = os.path.dirname(os.path.abspath(__file__))
  json_file_path = os.path.join(script_directory, '..',
                                'static/credentials.json')
  credentials = service_account.Credentials.from_service_account_file(
      json_file_path, scopes=['https://www.googleapis.com/auth/drive'])
  scopes = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
  ]
  # Load the credentials and create a service
  drive_service = build('drive',
                        'v3',
                        credentials=credentials,
                        static_discovery=False)
  docs_service = build('docs',
                       'v1',
                       credentials=credentials,
                       static_discovery=False)
  end_index = start_index + new_line + len(title) + 1
  # Add the title text and apply the named style and custom font style
  requests = [{
    'insertText': {
      'location': {
        'index': start_index,
      },
      'text': "\n" * new_line + title + "\n",
    }
  }, {
    'updateParagraphStyle': {
      'range': {
        'startIndex': start_index + new_line,
        'endIndex': end_index - 1
      },
      'paragraphStyle': {
        'namedStyleType': named_style
      },
      'fields': 'namedStyleType'
    }
  }, {
    'updateTextStyle': {
      'range': {
        'startIndex': start_index + new_line,
        'endIndex': end_index - 1
      },
      'textStyle': {
        'weightedFontFamily': {
          'fontFamily': style['font']
        },
        'fontSize': {
          'magnitude': style['size'],
          'unit': 'PT'
        },
        'foregroundColor': {
          'color': {
            'rgbColor': style['color']
          }
        }
      },
      'fields': 'foregroundColor,weightedFontFamily,fontSize,bold'
    }
  }]
  docs_service.documents().batchUpdate(documentId=document_id,
                                       body={
                                         'requests': requests
                                       }).execute()
  return end_index+1