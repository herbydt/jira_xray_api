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
        return ticket_id, ticket_key

    def add_test_cases_to_test_plan(self, test_plan_id, test_ids):
        payload = "{\"query\":\"mutation {\\n addTestsToTestPlan(\\n issueId: \\\"" + test_plan_id + "\\\",\\n " \
                  "testIssueIds: [\\\"" + test_ids + "\\\"]\\n ) {\\n addedTests\\n " \
                  "warning\\n }\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)

    def get_test_plan_id_from_key(self, test_plan_key):
        payload = "{\"query\":\"{\\n getTestPlans(jql: \\\"key=" + test_plan_key + "\\\", limit: 1) {\\n results " \
                  "{\\n issueId\\n jira(fields: [\\\"key\\\"])\\n }\\n }\\n}\\n\",\"variables\":{}}"
        json_resp = self.xray_support.get_graphql(payload)
        return json_resp["data"]["getTestPlans"]["results"][0]["issueId"]


