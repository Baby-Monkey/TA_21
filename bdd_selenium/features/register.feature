Feature: Verify register functionality

  @test
  Scenario: Successfully register a user using only mandatory fields
    Given I am on the register page
    When I enter "Ana" in first name input field
    When I enter "Paval" in last name input field
    When I enter "hugnarognu@gufum.com" in email input field
    When I enter "test1234" in password input field
    When I enter "test1234" in confirm password input field
    When I click the register button
    Then I should see "Your registration completed" register message