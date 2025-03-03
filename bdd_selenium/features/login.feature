Feature: Test the login component

  Background: Open login page
    Given I am on the login page

  @smoke
  Scenario: Login with unregistered email
    When I enter "test@gmai.com" in the email field
    When I enter "pass123" in the password field
    And I click the login button
    Then I should see "No customer account found" message

  @smoke
  Scenario Outline: Login with invalid credentials
      When I enter "<email>" in the email field
      When I enter "<password>" in the password field
      And I click the login button
      Then I should see "<error>" message

  Examples:
    | email               | password   | error                    |
    |test@gmai.com        | pass123    | No customer account found|
    |valid.email@gmail.com| N/A        | No customer account found|


    @regression
    Scenario: Log in with valid username and password
      When I enter "pisay24742@calmpros.com" in the email field
      And I enter "test123" in the password field
      And I click the login button
      Then I should see the Logout button
      And I should see the MyAccout button

