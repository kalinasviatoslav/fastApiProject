from main import app
from fastapi.testclient import TestClient
import random
import string

client = TestClient(app)

len_of_vincode = 17


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


test_car = {"manufacturer_id": 0,
            "model_id": 0,
            "vin_code": get_random_string(len_of_vincode)}


def test_success_creation_of_car():
    response = client.post(
            "/v1/vehicle/",
            json=test_car
    )
    assert response.status_code == 200
    assert response.json()['vin_code'] == test_car['vin_code']


def test_it_raises_error_if_create_same_object_car_twice():
    text_error = 'file with this vincode already exist in db'
    response = client.post(
            "/v1/vehicle/",
            json=test_car
    )
    assert response.status_code == 404
    assert response.json()['detail'] == text_error


def test_read_main():
    answer = {"manufacturer_id": 1, "model_id": 1, "id": 11}
    created_car = client.get("/v1/vehicle/get/SCA1S684X4UX07444")
    assert created_car.status_code == 200
    assert created_car.json() == answer
