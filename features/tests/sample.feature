@behave
Feature: JIRA/XRAY - Test Execution Reporting

  Scenario: Test Plan and Test Execution Tickets are created
    Given the test plan ticket is created
    When the test execution ticket is created
    And the test execution is linked to the test plan
    When the test tickets from test set is added in the test plan
    And the test tickets from test set is added in the test execution

  Scenario: Test Plan Ticket is already created and Test Execution Ticket is created
    Given there is an existing test plan ticket (TEST-1235) created
    When the test execution ticket is created
    And the test execution is linked to the test plan
    When the test tickets from test set is added in the test plan
    And the test tickets from test set is added in the test execution

  Scenario: Test Plan Ticket is created and Test Execution Ticket is already created
    Given the test plan ticket is created
    When there is an existing test execution ticket (TEST-1234) created
    And the test execution is linked to the test plan
    When the test tickets from test set is added in the test plan
    And the test tickets from test set is added in the test execution
