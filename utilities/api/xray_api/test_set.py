from utilities.api.xray_api.xray_support import XraySupport


class XrayTestSet:

    def __init__(self, context):
        self.xray_support = XraySupport(context)

    def get_test_cases_from_test_set(self, test_set_key):
        payload = "{\"query\":\"{\\n getTestSets(jql: \\\"key=" + test_set_key + "\\\", limit: 1) {\\n " \
                  "results {\\n issueId\\n jira(fields: [\\\"key\\\"])\\n projectId\\n tests(limit: 100) {\\n total\\n"\
                  "results {\\n issueId\\n jira(fields: [\\\"key\\\"])\\n projectId\\n }\\n }\\n }\\n }\\n}\\n\"" \
                  ",\"variables\":{}}"
        json_resp = self.xray_support.get_graphql(payload)
        return json_resp["data"]["getTestSets"]["results"][0]["tests"]["results"]
