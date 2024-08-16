Feature: Concurrent creation of dogs in the system

  Scenario: Create multiple dogs concurrently
    Given I have a list of valid dog payloads
    When I send concurrent POST requests to create the dogs
    Then all responses should have a status code of 201
    And all responses should match the dog creation schema
