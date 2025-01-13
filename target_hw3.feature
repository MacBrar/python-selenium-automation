# Created by mbrar at 1/12/2025
Feature: Test that opens target.com, clicks on the cart icon and verifies that “Your cart is empty” message is shown and user can navigate to sign in page

 Scenario: User opens target.com and is shown “Your cart is empty” after clicking on the cart icon
   Given Open Target main page
   When User clicks the cart icon
   Then Verify “Your cart is empty” is shown

  Scenario: Verify that a logged out user can navigate to Sign In
    Given Open Target main page
    When User clicks Sign In, then clicks Sign in again from navigation menu
    Then Verify Sign In form opened