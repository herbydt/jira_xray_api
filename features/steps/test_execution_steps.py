from behave import given, when, step
from utilities.api.xray_api.test_execution import XrayTestExecution


@given('the test execution ticket is created')
@when('the test execution ticket is created')
def step_impl(context):
    summary = '(Insert Ticket Title Here)'
    xray_support = XrayTestExecution(context)
    test_execution = xray_support.create_test_execution(summary, context.project_key)
    context.test_execution_key = test_execution[1]
    context.test_execution_id = test_execution[0]


@given('there is an existing test execution ticket ({test_execution_key}) created')
@when('there is an existing test execution ticket ({test_execution_key}) created')
def step_impl(context, test_execution_key):
    xray_support = XrayTestExecution(context)
    context.test_execution_key = test_execution_key
    context.test_execution_id = xray_support.get_test_exec_id_from_key(test_execution_key)


@when('the test execution is linked to the test plan')
def step_impl(context):
    xray_support = XrayTestExecution(context)
    xray_support.add_test_execution_to_test_plan(context.test_plan_id, context.test_execution_id)

