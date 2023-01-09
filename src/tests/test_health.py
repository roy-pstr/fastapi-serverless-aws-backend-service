from fastapi.testclient import TestClient


def test_health(client: TestClient) -> None:
    """
    Test the ping health check
    """
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {
        "ping": "pong",
    }
