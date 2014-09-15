####google_drive

Uploading files to GOOGLE drive without a human interaction using python

- As Claudio (GOOGLE) mentioned in http://youtu.be/zJVCKvXtHtE?t=12m18s, we need to use some logic (client library) to sort your crendentials for reusing. Other wise on every execution of `quickstart.py` script, you need human interaction for getting tokens. 
- I added 6 lines to google's `quickstart.py` to keep authorization code for reusing. So as long as the user has not revoked the access granted initially to the application, we don't need a human interaction. (https://developers.google.com/accounts/docs/OAuth2InstalledApp#refresh)
- For those who don't know what is this `quickstart.py`: *This script is a demo script made by GOOGLE for helping developers to get familiar with Google Drive SDK. More info available in https://developers.google.com/drive/quickstart-python*
- What google's `quickstart.py` is doing: *It is just uploading a filed named document.txt to google drive.*
- Before running (need only on first execution) this script, you need to setup a webserver running in local machine or just change the `REDIRECT_URI` to `urn:ietf:wg:oauth:2.0:oob`. Refer google's documentation for more details. I setup a instant webserver using following. *(This will setup a webserver on port `8000`)*  

        python -m SimpleHTTPServer
