import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
import openai

openai.api_key = os.environ.get('OPEN_API_KEY')

def file_list(folder_id):
  try:
    results = []
    script_directory = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_directory, '..',
                                  'static/credentials.json')
    credentials = service_account.Credentials.from_service_account_file(
        json_file_path, scopes=['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=credentials)

    # List files in the folder.
    results = drive_service.files().list(q=f"'{folder_id}' in parents",
                                         pageSize=10,
                                         fields="files(id, name)").execute()
  except Exception as e:
    print(f"\n\n\ file_list: error {str(e)} \n\n")

  return results
