import pytest
import requests
from app.models.calculation import Calculation
from app.schemas.calculation import CalculationCreate

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture
def create_payload():
    return {
        "operation": "add",
        "a": 10,
        "b": 20
    }

# ---------------------------------------------------------
# BROWSE Calculations
# ---------------------------------------------------------
def test_browse_calculations(fastapi_server, db_session):
    # seed some data
    c1 = Calculation(operation="add", a=1, b=2, result=3)
    c2 = Calculation(operation="subtract", a=10, b=5, result=5)
    db_session.add_all([c1, c2])
    db_session.commit()

    url = f"{BASE_URL}/calculations/"
    response = requests.get(url)

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) >= 2  # at least the two items we added



# ---------------------------------------------------------
# INVALID operation
# ---------------------------------------------------------
def test_invalid_operation(fastapi_server):
    url = f"{BASE_URL}/calculations/"
    payload = {
        "operation": "square_root",  # invalid
        "a": 10,
        "b": 2
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 400
    assert "Invalid operation" in response.text


# ---------------------------------------------------------
# INVALID input type
# ---------------------------------------------------------
def test_invalid_input_type(fastapi_server):
    url = f"{BASE_URL}/calculations/"
    payload = {
        "operation": "add",
        "a": "not_a_number",
        "b": 10
    }

    response = requests.post(url, json=payload)
    assert response.status_code == 400  # FastAPI validation error