#!/usr/bin/python
# https://developers.google.com/drive/quickstart-python
#
# As Claudio (GOOGLE Developer) mentioned in http://youtu.be/zJVCKvXtHtE?t=12m18s,
# we need to use some logic (client library) to sort your crendentials for reusing.
# Other wise on every execution of 'quickstart.py', you need human interaction for getting credentials
#
# Suku John George

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage

# Copy your credentials from the APIs Console (https://code.google.com/apis/console/)
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
#REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
REDIRECT_URI = 'http://localhost:8000'

# Path to the file to upload
FILENAME = 'document.txt'

# Path to the crendentials
CRED_FILENAME = 'credentials'

### For storing token
storage = Storage(CRED_FILENAME)

if not storage.get():
    # Run through the OAuth flow and retrieve authorization code
    flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, REDIRECT_URI)
    authorize_url = flow.step1_get_authorize_url()
    print 'Go to the following link in your browser: ' + authorize_url
    code = raw_input('Enter verification code: ').strip()
    credentials = flow.step2_exchange(code)

    ### Storing access token and a refresh token in CRED_FILENAME
    storage.put(credentials)
else:
    ### Getting access_token,expires_in,token_type,Refresh_toke info from CRED_FILENAME to 'credentials'
    credentials = storage.get()

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
    'title': 'My document',
    'description': 'A test document',
    'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)
