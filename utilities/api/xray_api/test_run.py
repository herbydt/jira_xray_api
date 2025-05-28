from utilities.api.xray_api.xray_support import XraySupport
import os


class XrayTestExecution:

    def __init__(self, context):
        self.xray_support = XraySupport(context)

    def attach_evidence_to_test_run(self, test_run_id, file_path, file_name):
        """
        Attach evidence (zip file) to a specific Test Run.
        
        Args:
            test_run_id (str): The ID of the Test Run
            file_path (str): The path to the directory containing the evidence file
            file_name (str): The name of the zip file to attach
            
        Returns:
            dict: JSON response from the Xray API
        """
        # Construct the full file path
        full_file_path = os.path.join(file_path, file_name)
        
        # Prepare the GraphQL mutation for attaching evidence
        payload = {
            "query": """
            mutation($file: Upload!, $testRunId: String!) {
                attachEvidenceToTestRun(
                    file: $file,
                    testRunId: $testRunId
                ) {
                    id
                    filename
                    size
                }
            }
            """,
            "variables": {
                "testRunId": test_run_id
            }
        }
        
        # Prepare the file for upload
        files = {
            'file': (file_name, open(full_file_path, 'rb'), 'application/zip')
        }
        
        # Make the API request
        response = self.xray_support.post_graphql_with_files(payload, files)
        return response

    