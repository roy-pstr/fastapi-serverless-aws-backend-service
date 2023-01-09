def test_exceptions(client):
    """
    Tests all error handling sceneries that can occur in the application.
    """
    # HTTPException triggered by business logic.
    response = client.get("/exceptions/http_exception")
    assert response.status_code == 500
    assert response.json().get("detail") == "StarletteHTTPException raised from inside the endpoint."

    # ValidationError triggered by FastAPI type validation.
    response = client.get("/exceptions/type_validation_exception/5")
    assert response.status_code == 200
    response = client.get("/exceptions/type_validation_exception/5.5")
    assert response.status_code == 422

    # ValueError triggered by business logic.
    response = client.get("/exceptions/unhandled_exception")
    assert response.status_code == 500
    assert response.text == "Value error raised from inside the endpoint."

    # Status code 500 without raising an exception
    response = client.get("/exceptions/status_code/500")
    assert response.status_code == 500

    # Status code 400 without raising an exception
    response = client.get("/exceptions/status_code/400")
    assert response.status_code == 400

    # Status code 404 for not found route
    response = client.get("/this/route/not/exist")
    assert response.status_code == 404
