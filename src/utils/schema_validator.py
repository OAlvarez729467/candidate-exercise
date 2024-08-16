from jsonschema import validate, ValidationError


def validate_response(schema, response_json):
    try:
        validate(instance=response_json, schema=schema)
    except ValidationError as e:
        raise AssertionError(f"Response validation error: {e.message}")
