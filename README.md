# google_drive_downloader

Prerequisites for using Gooogle API:
Follow these steps to set up your Google account to work with Google Drive API.
   1) Go to Google Cloud console https://console.cloud.google.com/ and sign in with your Google account.
   2) Create a new project.
   3) Go to APIs and Services.
   4) Enable Google Drive API for this project from the Library tab.
   5) Go back to Dashboard and to the OAuth Consent screen and configure the Consent screen for your project.
   6) Select External and click on Create
   7) Enter the name of your application and your email address. Click save and continue. 
   8) Add your email address in Test users and save.
   9) Now go to Credentials.
   10) Click on Create credentials, and go to OAuth Client ID.
   11) Enter your application’s type, and click Create.
   12) Your Client ID will be created. Download it to your computer and save it as credentials.json


Step 1: Install the Google client library
To install the Google client library for Python, run the following command:

  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  
Step 2: Run the script as

  python down_gd.py < path to your credentials.json file >
  
  
For the first execution of the script, a consent page opens to allow access to your google drive files. Select our google account and allow it.

The script lists down all files in your google drive.

You can enter the one or multiple file ids from the list to download the files. The files will be downloaded to Downloaded_files folder.
