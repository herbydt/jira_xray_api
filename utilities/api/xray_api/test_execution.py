from utilities.api.xray_api.xray_support import XraySupport


class XrayTestExecution:

    def __init__(self, context):
        self.xray_support = XraySupport(context)

    def create_test_plan(self, summary, proj_key):
        summary = summary + "Test Execution"
        payload = "{\"query\":\"mutation {\\n createTestExecution(\\n testIssueIds: []\\n jira: {\\n fields: {\\n " \
                  "summary: \\\"" + summary + "\\\",\\n project: {key: \\\"" + proj_key + "\\\"} \\n }\\n }\\n ) {\\n "\
                  "testExecution {\\n issueId\\n jira(fields: [\\\"key\\\"])\\n }\\n warnings\\n " \
                  "}\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)
        ticket_id = json_resp["data"]["createTestExecution"]["testExecution"]["issueId"]
        ticket_key = json_resp["data"]["createTestExecution"]["testExecution"]["jira"]["key"]
        # {"data":{"createTestExecution":{"testExecution":{"issueId":"10013","jira":{"key":"TP-7"}},"warnings":[]}}}
        return ticket_id, ticket_key

