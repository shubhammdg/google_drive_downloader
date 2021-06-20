from Google import Create_Service
import io
from googleapiclient.http import MediaIoBaseDownload
import sys
import os

CLIENT_SECRET_FILE = sys.argv[1]
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def download_file(id, name):
    print("\nDownloading {0}".format(name))
    request = service.files().get_media(fileId=id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    fh.seek(0)
    if not os.path.exists('Downloaded_files'):
        os.mkdir('Downloaded_files') 
    with open('Downloaded_files//'+name, 'wb') as f:
        f.write(fh.read())
        f.close()


service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

resource = service.files()
result_dict = resource.list(pageSize=100, fields="files(id, name, mimeType)").execute()
file_list = result_dict.get('files')
file_dict = {}
full_filenames = []
for item in file_list:
    file_dict[item['id']] = item['name']

print(result_dict)
print("\nfileId \t\t\t\t\t filename")
print("-"*50)

for file in (file_list):
    if file['mimeType'] != 'application/vnd.google-apps.folder':
        print("{0} \t\t {1}".format(file['id'], file['name']))

#print(full_filenames)
Ids = input("\nEnter the fileIds for files you want to download(space separated for multiple files): ")
FileIds = Ids.split()

for id in (FileIds):
    filename = file_dict[id]
    download_file(id, filename)