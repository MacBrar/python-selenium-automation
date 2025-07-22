# Created by mbrar at 7/21/2025
Feature: Tests for product page

  Scenario: User can select colors
    Given Open target product A-54551690 page
    Then Verify user can click through colors

  Scenario: Mens jeans colors
    Given Open target jeans
    Then click colors and verify