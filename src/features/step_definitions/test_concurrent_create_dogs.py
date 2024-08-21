import pytest
from utils.api_client import APIClient
from utils.schema_validator import validate_response
from utils.schemas import dog_creation_schema
from utils.data_generator import generate_random_breed, generate_random_age, generate_random_name
from pytest_bdd import scenarios, given, when, then, parsers
from concurrent.futures import ThreadPoolExecutor, as_completed

scenarios('../scenarios/concurrent_creation.feature')


@pytest.fixture
def context():
    return {}


@given('I have a list of valid dog payloads')
def step_given_list_of_valid_dog_payloads(context):
    context['payloads'] = [
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()},
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()},
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()}
    ]


@when('I send concurrent POST requests to create the dogs')
def step_when_concurrent_post_create_dogs(context):
    client = APIClient()
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(client.post, '/dogs', payload) for payload in context['payloads']]
    context['responses'] = [future.result() for future in as_completed(futures)]


@then(parsers.cfparse('all responses should have a status code of {status_code:d}'))
def step_then_check_all_responses_status_code(context, status_code):
    for response in context['responses']:
        assert response.status_code == status_code, \
            f"Expected {status_code}, got {response.status_code}"


@then('all responses should match the dog creation schema')
def step_then_validate_all_dog_creation_schemas(context):
    for response in context['responses']:
        response_body = response.json()
        validate_response(dog_creation_schema, response_body)
