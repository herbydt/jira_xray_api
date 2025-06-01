from behave import given
import pandas as pd
import csv
import openai


@given('the initialize method is completed')
def step_impl(context):
    pass


@given('this step is ran')
def step_impl(context):
    sample_data = [['ABC', 123]]
    cols = ['Letters', 'Numbers']
    df = pd.DataFrame(sample_data, columns=cols)
    df.to_csv('resources/test_run_results/sample_csv.csv', index=False)
    print("Successful Run!!!!")


@given('this next step is ran')
def step_impl(context):
    with open('resources/test_run_results/sample_csv.csv', 'r') as content:
        results = pd.read_csv(content)
    print(results['Letters'][0])