from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_members():
    client = app.test_client()
    response = client.get("/members")
    assert response.status_code == 200

def test_programs():
    client = app.test_client()
    response = client.get("/programs")
    assert response.status_code == 200

def test_program_detail():
    client = app.test_client()
    response = client.get("/programs/Yoga")
    assert response.status_code == 200