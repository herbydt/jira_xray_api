from behave import given, when, step
from utilities.api.xray_api.support.test_set_support import TestSetSupport
from utilities.api.xray_api.test_plan import XrayTestPlan
from utilities.api.xray_api.test_execution import XrayTestExecution


@when('the test tickets from test set is added in the test plan')
def step_impl(context):
    xray_test_set_support = TestSetSupport(context)
    test_set_key = xray_test_set_support.get_test_set_key('brand', 'produ', 'test_p')
    tests_from_set = xray_test_set_support.get_test_cases_from_test_set(test_set_key)
    test_ids_from_set = xray_test_set_support.format_test_ids(tests_from_set)

    xray_test_plan_support = XrayTestPlan(context)
    xray_test_plan_support.add_test_cases_to_test_plan(context.test_plan_id, test_ids_from_set)


@when('the test tickets from test set is added in the test execution')
def step_impl(context):
    xray_test_set_support = TestSetSupport(context)
    test_set_key = xray_test_set_support.get_test_set_key('brand', 'produ', 'test_p')
    tests_from_set = xray_test_set_support.get_test_cases_from_test_set(test_set_key)
    test_ids_from_set = xray_test_set_support.format_test_ids(tests_from_set)

    xray_test_exec_support = XrayTestExecution(context)
    xray_test_exec_support.add_test_execution_to_test_plan(context.test_execution_id, test_ids_from_set)
