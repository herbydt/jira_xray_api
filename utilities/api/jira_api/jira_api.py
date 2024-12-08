import requests
from jira import JIRA


username = "herbert.tiano@gmail.com"
password = "ATATT3xFfGF0VUzaYQ-DeyxR7pnB-cY92Utt8e3Axiyb_MBn8VpwzmtHMdMzYbqvJpscjfc-vEVjnFU43FjIZX3EIDld-tGFWeo3JrFtovHFJ9xZT-YSQGdEOXiavkPCvsdsldTuG_ReRCik4re9aKGwo_E9fCaHliO7GVVAjqrX6akjtpTw-dM=F203AE5B"
server = 'https://htiano.atlassian.net'
options = {'server': server}


def add_attachment_v1():

    url = "https://htiano.atlassian.net/rest/api/3/issue/SCRUM-1/attachments"
    filename = 'photo_6237519028058963005_y11.jpg'

    payload = {}
    # files = [('file', (filename, open('C:\\Users\\Herby\\Downloads\\' + filename, 'rb'), 'text/plain'))]
    files = [('file', (filename, open('C:\\Users\\Herby\\Downloads\\' + filename, 'rb'), 'image/jpeg'))]

    headers = {'X-Atlassian-Token': 'nocheck',
               'Authorization': 'Basic aGVyYmVydC50aWFub0BnbWFpbC5jb206QVRBVFQzeEZmR0YwVlV6YVlRLURleXhSN3BuQi1jWTkyVXR0OGUzQXhpeWJfTUJuOFZwd3ptdEhNZE16WWJxdkpwc2NqZmMtdkVWam5GVTQzRmpJWlgzRUlEbGQtdEdGV2VvM0pyRnRvdkhGSjl4WlQtWVNRR2RFT1hpYXZrUEN2c2RzbGRUdUdfUmVSQ2lrNHJlOWFLR3dvX0U5ZkNhSGxpTzdHVlZBanFyWDZha2p0cFR3LWRNPUYyMDNBRTVC',
               'Cookie': 'atlassian.xsrf.token=a1e480737cbca781241cde2977c87565e3856700_lin'}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.status_code)


def add_attachment_v2():
    filename = 'photo_6237519028058963005_y11.jpg'
    jira = JIRA(options, basic_auth=(username, password))

    issue = jira.issue('SCRUM-1')

    with open('C:\\Users\\Herby\\Downloads\\' + filename, 'rb') as f:
        jira.add_attachment(issue=issue, attachment=f)


def create_issue():
    issue_dict = {'project': {'key': 'SCRUM'},
                  'summary': 'New Task 2 from jira-python',
                  'description': 'Look into this one',
                  'issuetype': {'name': 'Task'},
                  'assignee': {'accountId': '61c48160e7637900685f9039'},
                  'reporter': {'accountId': '61c48160e7637900685f9039'},
                  'labels': ['TEST1']}
    jira = JIRA(options, basic_auth=(username, password))
    jira.create_issue(fields=issue_dict)


create_issue()
