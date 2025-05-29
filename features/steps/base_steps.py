from behave import given, when, step
import pandas as pd
import csv


@given('the initialize method is completed')
def step_impl(context):
    pass


@given('this step is ran')
def step_impl(context):
    sample_data = [['ABC', 123]]
    cols = ['Letters', 'Numbers']
    df = pd.DataFrame(sample_data, columns=cols)
    df.to_csv('output/outputs/sample_csv.csv', index=False)
    print("Successful Run!!!!")