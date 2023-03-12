from fastapi.testclient import TestClient


def test_root_route(client: TestClient) -> None:
    """
    Test the root route
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from api v2!",
    }
