from Google import Create_Service
import io
from googleapiclient.http import MediaIoBaseDownload
import sys
import os

try:
    CLIENT_SECRET_FILE = sys.argv[1]
except:
    print("\nPlease specify the credentials file as parameter")

API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def download_file(id, name):
    if not os.path.exists('Downloaded_files'):
        os.mkdir('Downloaded_files')
    print("\nDownloading {0}".format(name))
    try:
        request = service.files().get_media(fileId=id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print ("Download %d%%." % int(status.progress() * 100))
    except Exception as e:
        print(e)
        print("\nDownload Failed")
    try:
        fh.seek(0)
        with open('Downloaded_files//'+name, 'wb') as f:
            f.write(fh.read())
            f.close()
    except Exception as e:
        print(e)
        print("\nUnable to write downloaded file")

def service_connection():
    try:
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        return service
    except Exception as e:
        print(e)
        print("\nConnection failed")
        exit(1)

def get_file_list(service):
    try:
        resource = service.files()
        result_dict = resource.list(pageSize=100, fields="files(id, name, mimeType)").execute()
        file_list = result_dict.get('files')
        file_dict = {}
        for item in file_list:
                file_dict[item['id']] = item['name']
        return file_list, file_dict
    except Exception as e:
        print(e)
        print("\nUnable to fetch files")
        exit(1)

def print_files(file_list):
    print("\nfileId \t\t\t\t\t filename")
    print("-"*50)

    for file in (file_list):
            if file['mimeType'] != 'application/vnd.google-apps.folder':
                        print("{0} \t\t {1}".format(file['id'], file['name']))

service = service_connection()
file_list, file_dict = get_file_list(service)

print_files(file_list)

while True:
    Ids = input("\nEnter the fileIds for files you want to download(space separated for multiple files): ")
    FileIds = Ids.split()

    for id in (FileIds):
        if id in file_dict.keys():
            filename = file_dict[id]
            download_file(id, filename)
            more = input("\n Do you want to dowload more files (y/n): ")
            if more == 'n':
                exit(1)
        else:
            print("\nID not found\n")
