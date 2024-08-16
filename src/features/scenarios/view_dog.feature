Feature: View a dog in the system

  Scenario: View a dog successfully
    Given I have a valid dog ID
    When I send a GET request to view the dog
    Then the response status code should be 200
    And the response should match the dog retrieval schema

  Scenario: Fail to view a dog due to non-existing ID
    Given I have a non-existing dog ID
    When I send a GET request to view the dog
    Then the response status code should be 404
    And the response body should contain "Dog not found"
