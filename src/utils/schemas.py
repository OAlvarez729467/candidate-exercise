dog_creation_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "breed": {"type": "string"},
        "age": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "breed", "age", "name"]
}

dog_retrieval_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "breed": {"type": "string"},
        "age": {"type": "integer"},
        "name": {"type": "string"}
    },
    "required": ["id", "breed", "age", "name"]
}
