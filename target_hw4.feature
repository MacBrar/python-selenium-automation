# Created by mbrar at 1/13/2025
Feature: Verify there are at least 10 benefit cells and check if a product can be added to Target's cart

  Scenario: Verify there are at least 10 benefit cells
    Given Open Target Circle main page
    When Open Target Circle main page is opened
    Then Verify there are at least 10 benefit cells

  Scenario: Verify an item was added to cart
    Given Open Target main page
    When Search for tree
    Then Item can be added to cart