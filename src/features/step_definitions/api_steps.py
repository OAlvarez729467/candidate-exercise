from behave import given, when, then
from utils.api_client import APIClient
from utils.schema_validator import validate_response
from utils.schemas import dog_creation_schema, dog_retrieval_schema
from utils.data_generator import generate_random_breed, generate_random_age, generate_random_name


@given('I have a valid dog payload')
def step_given_valid_dog_payload(context):
    context.payload = {
        "breed": generate_random_breed(),
        "age": generate_random_age(),
        "name": generate_random_name()
    }


@given('I have an incomplete dog payload')
def step_given_incomplete_dog_payload(context):
    context.payload = {
        "breed": generate_random_breed()
        # Missing 'age' and 'name
    }


@given('I have a dog payload with incorrect data types')
def step_given_dog_payload_incorrect_data_types(context):
    context.payload = {
        "breed": generate_random_breed(),
        "age": "three",  # Must be int
        "name": 12345    # Must be string
    }


@given('I have a dog payload with extra fields')
def step_given_dog_payload_extra_fields(context):
    context.payload = {
        "breed": generate_random_breed(),
        "age": generate_random_age(),
        "name": generate_random_name(),
        "color": "Golden"  # Extra field
    }


@given('I have a valid dog ID')
def step_given_valid_dog_id(context):
    context.dog_id = 1  # We assume that ID 1 exists


@given('I have a non-existing dog ID')
def step_given_non_existing_dog_id(context):
    context.dog_id = 99999  # We assume that this ID does not exist


@given('I have a list of valid dog payloads')
def step_given_list_of_valid_dog_payloads(context):
    context.payloads = [
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()},
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()},
        {"breed": generate_random_breed(), "age": generate_random_age(), "name": generate_random_name()}
    ]


@when('I send a POST request to create the dog')
def step_when_post_create_dog(context):
    context.response = APIClient().post('/dogs', context.payload)


@when('I send a GET request to view the dog')
def step_when_get_view_dog(context):
    context.response = APIClient().get(f'/dogs/{context.dog_id}')


@when('I send a DELETE request to delete the dog')
def step_when_delete_dog(context):
    context.response = APIClient().delete(f'/dogs/{context.dog_id}')


@when('I send concurrent POST requests to create the dogs')
def step_when_concurrent_post_create_dogs(context):
    client = APIClient()
    context.responses = [client.post('/dogs', payload) for payload in context.payloads]


@then('the response status code should be {status_code:d}')
def step_then_check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"


@then('the response body should contain "{expected_value}"')
def step_then_check_response_body_contains(context, expected_value):
    assert expected_value in context.response.text, \
        f"Expected '{expected_value}' in response body, got {context.response.text}"


@then('the response should match the dog creation schema')
def step_then_validate_dog_creation_schema(context):
    response_body = context.response.json()
    validate_response(dog_creation_schema, response_body)


@then('the response should match the dog retrieval schema')
def step_then_validate_dog_retrieval_schema(context):
    response_body = context.response.json()
    validate_response(dog_retrieval_schema, response_body)


@then('all responses should have a status code of {status_code:d}')
def step_then_check_all_responses_status_code(context, status_code):
    for response in context.responses:
        assert response.status_code == status_code, f"Expected {status_code}, got {response.status_code}"


@then('all responses should match the dog creation schema')
def step_then_validate_all_dog_creation_schemas(context):
    for response in context.responses:
        response_body = response.json()
        validate_response(dog_creation_schema, response_body)
