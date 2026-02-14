from app import app

def test_home_returns_200_and_message():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json()["message"] == "Hello from DevOps project!"

def test_products_returns_list_with_two_items():
    client = app.test_client()
    resp = client.get("/products")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 2
