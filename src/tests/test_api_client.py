from utils.api_client import APIClient


def test_api_client_get_request():
    client = APIClient()
    response = client.get("/dogs")
    assert response.status_code == 200
