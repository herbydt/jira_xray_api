from behave import given, when, step


@given('the initialize method is completed')
def step_impl(context):
    pass


@given('this step is ran')
def step_impl(context):
    print("Successful Run!!!!")