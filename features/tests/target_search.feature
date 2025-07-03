# Created by mbrar at 7/2/2025
Feature: Tests for search
"""
  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown
"""
  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown