from utilities.api.xray_api.xray_support import XraySupport


class XrayTestPlan:

    def __init__(self, context):
        self.xray_support = XraySupport(context)

    def create_test_plan(self, summary, proj_key):
        summary = summary + "Test Plan"
        payload = "{\"query\":\"mutation {\\n createTestPlan(\\n testIssueIds: []\\n jira: {\\n fields: {\\n summary:" \
                  "\\\"" + summary + "\\\",\\n project: {key: \\\"" + proj_key + "\\\"} \\n }\\n }\\n ) {\\n testPlan" \
                  "{\\n issueId\\n jira(fields: [\\\"key\\\"])\\n }\\n warnings\\n }\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)
        ticket_id = json_resp["data"]["createTestPlan"]["testPlan"]["issueId"]
        ticket_key = json_resp["data"]["createTestPlan"]["testPlan"]["jira"]["key"]
        # {"data":{"createTestPlan":{"testPlan":{"issueId":"10012","jira":{"key":"TP-6"}},"warnings":[]}}}
        return ticket_id, ticket_key

