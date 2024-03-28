from os.path import dirname
import pandas as pd


class TestExecSupport:

    def read_test_results(self):
        project_root = dirname(dirname(dirname(dirname(__file__))))
        with open(project_root + '\\resources\\test_results\\test_results.csv', 'r') as body:
            test_results_df = pd.read_csv(body)
        return test_results_df
