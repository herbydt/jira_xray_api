from dotenv import load_dotenv
import os
import json
import requests
from utilities.endpoints.endpoints import BaseUrls, XrayEndpoints


class XrayToken:

    def __init__(self):
        self.url = BaseUrls().xray
        self.xray_endpoints = XrayEndpoints()

    def generate_token(self, client_id, client_secret):
        load_dotenv()
        url = self.url + self.xray_endpoints.auth
        payload = json.dumps({"client_id": client_id,
                              "client_secret": client_secret})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text.replace('"', '')

