Feature: Test the products functionality

  Background: Navigate to products page with standard user
    Given I am on the products page as standard user

  @products
  Scenario: Products are sorted alphabetically
    Then Products names are sorted alphabetically

  @products2
  Scenario: Products are sorted by price (low to high)
    When I sort the products "Price (low to high)"
    Then Products are sorted by price from low to high

  @products3
  Scenario: Product is added to cart
    When I click the add to cart button
    Then The button name chage to Remove
    And Item number "1" is displayed on the cart