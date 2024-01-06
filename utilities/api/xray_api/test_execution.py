from utilities.api.xray_api.xray_support import XraySupport


class XrayTestExecution:

    def __init__(self, context):
        self.xray_support = XraySupport(context)

    def create_test_execution(self, summary, proj_key):
        summary = summary + " - Test Execution"
        payload = "{\"query\":\"mutation {\\n createTestExecution(\\n testIssueIds: []\\n jira: {\\n fields: {\\n " \
                  "summary: \\\"" + summary + "\\\",\\n project: {key: \\\"" + proj_key + "\\\"} \\n }\\n }\\n ) {\\n "\
                  "testExecution {\\n issueId\\n jira(fields: [\\\"key\\\"])\\n }\\n warnings\\n " \
                  "}\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)
        ticket_id = json_resp["data"]["createTestExecution"]["testExecution"]["issueId"]
        ticket_key = json_resp["data"]["createTestExecution"]["testExecution"]["jira"]["key"]
        return ticket_id, ticket_key

    def add_test_execution_to_test_plan(self, test_plan_id, test_exec_id):
        payload = "{\"query\":\"mutation {\\n addTestExecutionsToTestPlan(\\n issueId: \\\"" + test_plan_id + "\\\"," \
                  "\\n testExecIssueIds: [\\\"" + test_exec_id + "\\\"]\\n ) {\\n addedTestExecutions\\n " \
                  "warning\\n }\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)

    def add_test_cases_to_test_execution(self, test_exec_id, test_ids):
        payload = "{\"query\":\"mutation {\\n addTestsToTestExecution(\\n issueId: \\\"" + test_exec_id + "\\\",\\n " \
                  "testIssueIds: [\\\"" + test_ids + "\\\"]\\n ) {\\n addedTests\\n " \
                  "warning\\n }\\n}\",\"variables\":{}}"
        json_resp = self.xray_support.post_graphql(payload)

    def get_test_exec_id_from_key(self, test_exec_key):
        payload = "{\"query\":\"{\\n getTestExecutions(jql: \\\"key=" + test_exec_key + "\\\", limit: 1) {\\n results "\
                  "{\\n issueId\\n jira(fields: [\\\"key\\\"])\\n }\\n }\\n}\\n\",\"variables\":{}}"
        json_resp = self.xray_support.get_graphql(payload)
        return json_resp["data"]["getTestExecutions"]["results"][0]["issueId"]
