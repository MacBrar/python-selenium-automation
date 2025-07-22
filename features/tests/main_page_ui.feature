# Created by mbrar at 7/21/2025
Feature: Tests for Main page UI

  Scenario: User can see correct amount of header links
    Given Open target circle main page
    Then Verify 10 header links are shown
