from behave import given, when, step
from utilities.api.xray_api.test_plan import XrayTestPlan


@given('the test plan ticket is created')
@when('the test plan ticket is created')
def step_impl(context):
    summary = '(Insert Ticket Title Here)'
    xray_support = XrayTestPlan(context)
    test_plan = xray_support.create_test_plan(summary, context.project_key)
    context.test_plan_key = test_plan[1]
    context.test_plan_id = test_plan[0]


@given('there is an existing test plan ticket ({test_plan_key}) created')
@when('there is an existing test plan ticket ({test_plan_key}) created')
def step_impl(context, test_plan_key):
    xray_support = XrayTestPlan(context)
    context.test_plan_key = test_plan_key
    context.test_plan_id = xray_support.get_test_plan_id_from_key(test_plan_key)



