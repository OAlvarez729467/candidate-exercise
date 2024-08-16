Feature: Create a dog in the system

  Scenario: Create a dog successfully
    Given I have a valid dog payload
    When I send a POST request to create the dog
    Then the response status code should be 201
    And the response should match the dog creation schema

  Scenario: Fail to create a dog due to incomplete payload
    Given I have an incomplete dog payload
    When I send a POST request to create the dog
    Then the response status code should be 400
    And the response body should contain "Missing fields"

  Scenario: Fail to create a dog due to incorrect data type
    Given I have a dog payload with incorrect data types
    When I send a POST request to create the dog
    Then the response status code should be 400
    And the response body should contain "Invalid data type"

  Scenario: Create a dog with extra fields
    Given I have a dog payload with extra fields
    When I send a POST request to create the dog
    Then the response status code should be 201
    And the response should match the dog creation schema
