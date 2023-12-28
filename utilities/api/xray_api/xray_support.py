import requests
import json
from utilities.endpoints.endpoints import BaseUrls
from utilities.endpoints.endpoints import XrayEndpoints


class XraySupport:

    def __init__(self, context):
        self.url = BaseUrls().xray
        self.xray_endpoints = XrayEndpoints()
        self.graph_url = self.url + self.xray_endpoints.graphql
        self.token = context.xray_token

    def post_graphql(self, payload):
        headers = {'Authorization': 'Bearer ' + self.token,
                   'Content-Type': 'application/json'}
        response = requests.request("POST", self.graph_url, headers=headers, data=payload, verify=False)
        json_resp = json.loads(response.text)
        return json_resp

    def get_graphql(self, payload):
        headers = {'Authorization': 'Bearer ' + self.token,
                   'Content-Type': 'application/json'}
        response = requests.request("GET", self.graph_url, headers=headers, data=payload, verify=False)
        json_resp = json.loads(response.text)
        return json_resp
