import os, json
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

def service():
    raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON")
    if not raw:
        raise RuntimeError("GOOGLE_SERVICE_ACCOUNT_JSON is missing")
    info = json.loads(raw)
    creds = service_account.Credentials.from_service_account_info(info, scopes=SCOPES)
    return build("drive", "v3", credentials=creds, cache_discovery=False)

def list_files(folder_id):
    svc = service()
    q = f"'{folder_id}' in parents and trashed=false"
    return svc.files().list(q=q, fields="files(id,name,mimeType,modifiedTime,size)").execute().get("files", [])

def download_file(file_id, target_dir="/tmp/kapasita"):
    target = Path(target_dir); target.mkdir(parents=True, exist_ok=True)
    svc = service()
    meta = svc.files().get(fileId=file_id, fields="name").execute()
    path = target / meta["name"]
    req = svc.files().get_media(fileId=file_id)
    with path.open("wb") as fh:
        dl = MediaIoBaseDownload(fh, req)
        done = False
        while not done:
            _, done = dl.next_chunk()
    return path
