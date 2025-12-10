""" Testing all Conditions API Routes"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.conditions_router import router
from uuid import uuid4

app = FastAPI()
app.include_router(router)
client = TestClient(app)


# ------------------------------------------------------#
# Test for getting all conditions
# ------------------------------------------------------#


def test_get_all_conditions_returns_list_and_200(mocker):
    fake_conditions = [
        {
            "id": uuid4(),
            "encounter_id": uuid4(),
            "medical_condition": "Hypertension",
            "created_at": "2023-09-15T09:00:00Z",
            "icd10_code": "I10",
        },
        {
            "id": uuid4(),
            "encounter_id": uuid4(),
            "medical_condition": "Diabetes Mellitus",
            "created_at": "2023-08-20T11:30:00Z",
            "icd10_code": "E11",
        },
    ]

    mocker.patch(
        "app.api.v1.conditions_router.service_get_all_conditions",
        return_value=fake_conditions,
    )

    response = client.get("/conditions/")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["medical_condition"] == "Hypertension"


# ------------------------------------------------------#
# Test for getting conditions by encounter ID
# ------------------------------------------------------#
def test_get_conditions_by_encounter_id_returns_list_and_200(mocker):
    fake_conditions = [
        {
            "id": uuid4(),
            "encounter_id": uuid4(),
            "medical_condition": "Asthma",
            "created_at": "2023-07-10T10:00:00Z",
            "icd10_code": "J45",
        },
        {
            "id": uuid4(),
            "encounter_id": uuid4(),
            "medical_condition": "Chronic Bronchitis",
            "created_at": "2023-06-05T12:15:00Z",
            "icd10_code": "J42",
        },
    ]

    mocker.patch(
        "app.api.v1.conditions_router.service_get_conditions_by_encounter_id",
        return_value=fake_conditions,
    )

    encounter_id = fake_conditions[0]["encounter_id"]
    response = client.get(f"/conditions/by-encounter/{encounter_id}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["medical_condition"] == "Asthma"
