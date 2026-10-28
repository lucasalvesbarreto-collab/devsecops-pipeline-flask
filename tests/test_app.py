from app.main import app


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_greet():
    client = app.test_client()
    response = client.get("/api/greet?name=Lucas")
    assert response.status_code == 200
    assert "Lucas" in response.get_json()["message"]