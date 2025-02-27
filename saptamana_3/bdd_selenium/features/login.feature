Feature: Test the login component

  Scenario: Login with unregistered email
    Given I am on the login page
    When I enter "test@gmai.com" in the email field
    When I enter "pass123" in the password field
    And I click the login button
    Then I should see "No customer account found" message