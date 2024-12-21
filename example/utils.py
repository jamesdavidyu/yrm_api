from dotenv import load_dotenv
import os
from google.oauth2 import id_token
from google.auth.transport import requests

load_dotenv()

def verify_google_access_token(token):
    try:
        CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
        request = requests.Request()
        idinfo = id_token.verify_oauth2_token(token, request, CLIENT_ID) 

        return idinfo
    except ValueError as e:
        return None