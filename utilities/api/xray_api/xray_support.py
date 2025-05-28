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

    def xray_header(self):
        headers = {'Authorization': 'Bearer ' + self.token,
                   'Content-Type': 'application/json'}
        return headers

    def post_graphql(self, payload):
        response = requests.request("POST", self.graph_url, headers=self.xray_header(), data=payload, verify=False)
        json_resp = json.loads(response.text)
        return json_resp

    def post_graphql_with_files(self, payload, files):
        """
        Send a GraphQL request with file uploads.
        
        Args:
            payload (dict): The GraphQL query and variables
            files (dict): Files to be uploaded
            
        Returns:
            dict: JSON response from the API
        """
        # Remove Content-Type header to let requests set it automatically for multipart/form-data
        headers = {'Authorization': 'Bearer ' + self.token}
        
        # Convert the payload to a string
        operations = json.dumps(payload)
        
        # Prepare the multipart form data
        data = {
            'operations': operations,
            'map': json.dumps({"0": ["variables.file"]})
        }
        
        # Make the request
        response = requests.post(
            self.graph_url,
            headers=headers,
            data=data,
            files=files,
            verify=False
        )
        
        return json.loads(response.text)

    def get_graphql(self, payload):
        response = requests.request("GET", self.graph_url, headers=self.xray_header(), data=payload, verify=False)
        json_resp = json.loads(response.text)
        return json_resp

    def import_xray_json_report(self, reports_json):
        url = self.url + self.xray_endpoints.import_results
        payload = json.dumps(reports_json)
        response = requests.request("POST", url, headers=self.xray_header(), data=payload, verify=False)
