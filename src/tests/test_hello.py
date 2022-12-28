from fastapi.testclient import TestClient

def test_root_route(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from your backend service running on your local machine!",
    }