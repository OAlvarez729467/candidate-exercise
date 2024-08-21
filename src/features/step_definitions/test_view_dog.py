import pytest
from utils.api_client import APIClient
from utils.schema_validator import validate_response
from utils.schemas import dog_retrieval_schema
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../scenarios/view_dog.feature')


@pytest.fixture
def context():
    return {}


@given('I have fetched an existing dog ID')
def step_given_fetched_existing_dog_id(context):
    response = APIClient().get('/dogs')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    dogs = response.json()
    first_dog_id = next(iter(dogs.keys()))
    context['dog_id'] = first_dog_id


@given('I have a non-existing dog ID')
def step_given_non_existing_dog_id(context):
    context['dog_id'] = 99999  # Assume this ID does not exist


@when('I send a GET request to view the dog')
def step_when_get_view_dog(context):
    context['response'] = APIClient().get(f'/dogs/{context["dog_id"]}')


@then(parsers.cfparse('the response status code should be {status_code:d}'))
def step_then_check_status_code(context, status_code):
    assert context['response'].status_code == status_code, \
        f"Expected {status_code}, got {context['response'].status_code}"


@then(parsers.cfparse('the response body should contain "{expected_value}"'))
def step_then_check_response_body_contains(context, expected_value):
    assert expected_value in context['response'].text, \
        f"Expected '{expected_value}' in response body, got {context['response'].text}"


@then('the response should match the dog retrieval schema')
def step_then_validate_dog_retrieval_schema(context):
    response_body = context['response'].json()
    validate_response(dog_retrieval_schema, response_body)
