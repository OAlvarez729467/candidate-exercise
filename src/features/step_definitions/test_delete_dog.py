import pytest
from utils.api_client import APIClient
from pytest_bdd import scenarios, given, when, then, parsers
from utils.data_generator import generate_random_breed, generate_random_age, generate_random_name

scenarios('../scenarios/delete_dog.feature')


@pytest.fixture
def context():
    return {}


@given('I have created a new dog')
def step_given_created_new_dog(context):
    payload = {
        "breed": generate_random_breed(),
        "age": generate_random_age(),
        "name": generate_random_name()
    }
    response = APIClient().post('/dogs', payload)
    context['dog_id'] = response.json().get('id')
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


@given('I have a non-existing dog ID')
def step_given_non_existing_dog_id(context):
    context['dog_id'] = 99999  # Assume this ID does not exist


@when('I send a DELETE request to delete the dog')
def step_when_delete_dog(context):
    context['response'] = APIClient().delete(f'/dogs/{context["dog_id"]}')


@then(parsers.cfparse('the response status code should be {status_code:d}'))
def step_then_check_status_code(context, status_code):
    assert context['response'].status_code == status_code, \
        f"Expected {status_code}, got {context['response'].status_code}"


@then(parsers.cfparse('the response body should contain "{expected_value}"'))
def step_then_check_response_body_contains(context, expected_value):
    assert expected_value in context['response'].text, \
        f"Expected '{expected_value}' in response body, got {context['response'].text}"
