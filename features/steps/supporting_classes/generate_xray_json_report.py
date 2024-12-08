import pandas as pd
from datetime import datetime
from utilities.util.utilities_dataframe import *
from utilities.util.utilities_data import *


class GenerateXrayJsonReport:

    def __init__(self):
        self.path = 'resources/test_results/'

    def generate_xray_report(self, test_exec_key):
        with open(self.path + 'test_results.csv', 'r') as content:
            report = pd.read_csv(content)
        df_values = []
        test_tickets = list(report['Test Ticket'].unique())
        df_values = self.generate_report_df(test_tickets, report, df_values)
        summary = pd.DataFrame(df_values, columns=['testKey', 'status', 'iteration', 'comment', 'defect'])
        return xray_import_report_json(summary, test_exec_key)

    def generate_report_df(self, test_tickets, report_df, df_values):
        for test in test_tickets:
            final_status = 'PASSED'
            fail_count = 0
            final_comment = ''
            iter_json = []
            dup_checker_list = []
            defect = ''
            status = ''
            iter_count = 0
            for i, row in report_df.iterrows():
                comment = replace_nan_values(row['Comments'])
                iter_cols = row.index.tolist()
                iter_cols.remove('Test Ticket')
                iter_json, iter_count, dup_checker_list = iter_support(row, test, iter_cols, iter_json,
                                                                       iter_count, dup_checker_list)

                if row['Test Ticket'] == test and row['Status'] == 'failed':
                    defect, status = self.get_existing_defect(row['Test Ticket'])
                    fail_count = fail_count + 1
                    if final_comment == '':
                        final_comment = 'FAILED SCENARIOS: \n \n'
                    final_comment = final_comment + ' TEST'

            if fail_count > 0:
                final_status = 'FAILED'
                if defect:
                    final_status = status

            df_values.append([test, final_status, iter_json, str(final_comment), defect])
            return df_values

    def get_existing_defect(self, test_ticket):
        defect_mapping = pd.read_csv(self.path + 'issue_mapping.csv')
        defect_df = filter_by_col_values(defect_mapping, ('Test Ticket', test_ticket))
        defect_list = defect_df['Issue Ticket'].values.tolist()
        status = get_result_generic(defect_mapping, 'Status', ('Test Ticket', test_ticket))

        if not defect_list:
            return None, None
        else:
            return defect_list, status


def xray_import_report_json(summary, test_exec_key):
    today = datetime.now()
    start = today.strftime("%Y-%m-%d") + "T" + today.strftime("%H:%M") + "00+01:00"
    finish = today.strftime("%Y-%m-%d") + "T" + today.strftime("%H:%M") + "30+01:00"
    new_entry = []
    for i, row in summary.iterrows():
        iteration = row['iteration']
        defect = []
        if row['defect']:
            defect = row['defect']
        new_entry.append({"test_ket": row['testKey'],
                          "start": start,
                          "finish": finish,
                          "comment": str(row['comment']),
                          "status": row['status'].upper(),
                          "defects": defect,
                          "iterations": iteration})
    json_report = {"testExecutionKey": test_exec_key,
                   "tests": new_entry}
    return json_report


def iter_support(row, test, iter_cols, iter_json, iter_count, dup_checker_list):
    if iter_count < 1000 and row['Test Ticket'] == test:
        dup_check = ''
        params = []
        for df_row in iter_cols:
            dup_check = dup_check + str(row[df_row])
            iter_data = {"name": df_row,
                         "value": replace_nan_values(row[df_row])}
            params.append(iter_data)

        if dup_check not in dup_checker_list:
            dup_checker_list.append(dup_check)
            json_obj = {"parameters": params,
                        "status": row['Status'].upper()}
            iter_json.append(json_obj)
            iter_count = iter_count + 1
    return iter_json, iter_count, dup_checker_list
