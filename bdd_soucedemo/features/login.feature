Feature: Test the login functionality

  Background: Open the login page
    Given I am on the login page

  @login
  Scenario: Login as standard user with valid credentials
    When Enter "standard_user" in the username field
    When Enter "secret_sauce" in the password field
    When Click the login button
    Then I should see the "Products" page title
    Then The url of the current page is "https://www.saucedemo.com/inventory.html"