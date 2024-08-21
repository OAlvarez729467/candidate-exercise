Feature: Delete a dog from the system

  Scenario: Delete a dog successfully
    Given I have created a new dog
    When I send a DELETE request to delete the dog
    Then the response status code should be 200

  Scenario: Fail to delete a dog due to non-existing ID
    Given I have a non-existing dog ID
    When I send a DELETE request to delete the dog
    Then the response status code should be 404
    And the response body should contain "Doggo Not Found"
