from __future__ import print_function

import os.path
import base64

from datetime import datetime
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']


def send_email(email, county, threshhold, percentile, new_person = False):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './src/Email/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        
        message = EmailMessage()

        if new_person:
            f = open('./src/Email/welcomeEmail.txt', "r")
        else:
            f = open('./src/Email/emailContent.txt', "r")
        content = f.read()
        f.close()
        # print("File read")

        today = datetime.now()
        content = content.replace("[$$Date$$]", str(today.day) + " " + str(today.strftime("%B")) + " " + str(today.year) + ",")
        content = content.replace("[$$County$$]", county + " County")
        if new_person:
            content = content.replace("[$$Threshhold$$]", threshhold + "%")
        content = content.replace("[$$Percentile$$]", str(percentile) + "%")

        message['To'] = email #'dnanavati@scu.edu'
        message['From'] = 'covidalerts2023@gmail.com'
        if new_person:
            message['Subject'] = 'Welcome to Water Watcher Alerts'
        else:
            message['Subject'] = 'Your COVID-19 Breakdown'
        message.add_header('Content-Type','text/html')
        message.set_payload(content)

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_string().encode('utf-8')).decode()

        create_message = {
            'raw': encoded_message
        }
        
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        # print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    e = "dnanavati@scu.edu"
    c = "Fresno"
    t = "70"
    p = "76.51"
    send_email(e, c, t, p, True)