# Tests all error handling sceneries that can occur in the application.
from fastapi.testclient import TestClient

from src.main import app


def test_http_exception(client):
    """HTTPException triggered by business logic."""
    response = client.get("/exceptions/http_exception")
    assert response.status_code == 500
    assert response.json().get("detail") == "StarletteHTTPException raised from inside the endpoint."


def test_validation_error(client):
    """ValidationError triggered by FastAPI type validation."""
    response = client.get("/exceptions/type_validation_exception/5")
    assert response.status_code == 200
    response = client.get("/exceptions/type_validation_exception/5.5")
    assert response.status_code == 422


def test_unhandled_exception():
    """ValueError triggered by business logic."""
    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/exceptions/unhandled_exception")
        assert response.status_code == 500
        assert response.text == "Value error raised from inside the endpoint."


def test_http_exception_500(client):
    """Status code 500 without raising an exception"""
    response = client.get("/exceptions/status_code/500")
    assert response.status_code == 500


def test_http_exception_400(client):
    """Status code 400 without raising an exception"""
    response = client.get("/exceptions/status_code/400")
    assert response.status_code == 400


def test_route_not_found(client):
    """Status code 404 for not found route"""
    response = client.get("/this/route/not/exist")
    assert response.status_code == 404
