import pytest
from utils.api_client import APIClient
from utils.schema_validator import validate_response
from utils.schemas import dog_creation_schema
from utils.data_generator import generate_random_breed, generate_random_age, generate_random_name
from pytest_bdd import scenarios, given, when, then, parsers

scenarios('../scenarios/create_dog.feature')


# Fixture to manage shared information
@pytest.fixture
def context():
    return {}


@given('I have a valid dog payload')
def step_given_valid_dog_payload(context):
    context['payload'] = {
        "breed": generate_random_breed(),
        "age": generate_random_age(),
        "name": generate_random_name()
    }


@given('I have an incomplete dog payload')
def step_given_incomplete_dog_payload(context):
    context['payload'] = {
        "breed": generate_random_breed()
        # Missing 'age' and 'name
    }


@given('I have a dog payload with incorrect data types')
def step_given_dog_payload_incorrect_data_types(context):
    context['payload'] = {
        "breed": generate_random_breed(),
        "age": "three",  # It should be an integer
        "name": 12345    # It should be a string
    }


@given('I have a dog payload with extra fields')
def step_given_dog_payload_extra_fields(context):
    context['payload'] = {
        "breed": generate_random_breed(),
        "age": generate_random_age(),
        "name": generate_random_name(),
        "color": "Golden"  # Extra field
    }


@when('I send a POST request to create the dog')
def step_when_post_create_dog(context):
    context['response'] = APIClient().post('/dogs', context['payload'])


@then(parsers.cfparse('the response status code should be {status_code:d}'))
def step_then_check_status_code(context, status_code):
    assert context['response'].status_code == status_code, \
        f"Expected {status_code}, got {context['response'].status_code}"


@then(parsers.cfparse('the response body should contain "{expected_value}"'))
def step_then_check_response_body_contains(context, expected_value):
    assert expected_value in context['response'].text, \
        f"Expected '{expected_value}' in response body, got {context['response'].text}"


@then('the response should match the dog creation schema')
def step_then_validate_dog_creation_schema(context):
    response_body = context['response'].json()
    validate_response(dog_creation_schema, response_body)
