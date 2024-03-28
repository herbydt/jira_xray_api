from os.path import dirname
import pandas as pd
from utilities.util.utilities_dataframe import filter_by_col_values
from utilities.api.xray_api.test_set import XrayTestSet


class TestSetSupport(XrayTestSet):

    def get_test_set_key(self, brand, product, test_phase):
        xray_api_root = dirname(dirname(__file__))
        with open(xray_api_root + '\\mapping_csv\\test_set_list.csv', 'r') as body:
            set_list = pd.read_csv(body)

        df = filter_by_col_values(set_list, ('Brand', brand), ('Product', product.upper()), ('Test_Phase', test_phase))
        test_set_key = df['Test_Set_Ticket'].values[0]
        return test_set_key

    def format_test_ids(self, tests_from_set):
        test_ids = ""
        i = 0
        for issue_id in tests_from_set:
            if i == 0:
                test_ids = test_ids + '\\\"' + str(issue_id["issueId"]) + '\\\"'
            if i > 0:
                test_ids = test_ids + ', \\\"' + str(issue_id["issueId"]) + '\\\"'
            i = i + 1
        return test_ids
