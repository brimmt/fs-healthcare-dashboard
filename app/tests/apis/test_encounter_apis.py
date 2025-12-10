from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.encounters_router import router
from uuid import uuid4

app = FastAPI()
app.include_router(router)

client = TestClient(app)

#------------------------------------------------------#
# Test for getting all encounters       
#------------------------------------------------------#
def test_get_all_encounters_returns_list_and_200(mocker):
    fake_encounters = [
        {"id": uuid4(),
         "patient_id": uuid4(), 
         "admission_date": "2023-10-01", 
         "discharge_date": "2023-10-10", 
         "doctor_name":"John Smith", 
         "hospital_name":"General Hospital",
         "insurance_provider":"Cigna",
         "billing_amount":1500.00,
         "room_number":101,
         "admission_type":"Emergency",
         "created_at":"2023-10-01T10:00:00Z"},

         {"id": uuid4(),
          "patient_id": uuid4(),
          "admission_date": "2023-11-05",
          "discharge_date": "2023-11-15",
          "doctor_name":"Emily Davis",
          "hospital_name":"City Medical Center",
          "insurance_provider":"Blue Cross",
          "billing_amount":2500.00,
          "room_number":202,
          "admission_type":"Elective",
          "created_at":"2023-11-05T14:30:00Z"},
    ]

    mocker.patch(
        "app.api.v1.encounters_router.service_get_all_encounters",
        return_value = fake_encounters,
    )

    response = client.get("/encounters/")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["doctor_name"] == "John Smith"


#------------------------------------------------------#
# Test for getting encounters by encounter ID
#------------------------------------------------------#
def test_get_encounter_by_id_returns_encounter_and_200(mocker):
    fake_encounter = {
        "id": uuid4(),
        "patient_id": uuid4(),
        "admission_date": "2023-10-01",
        "discharge_date": "2023-10-10",
        "doctor_name":"John Smith",
        "hospital_name":"General Hospital",
        "insurance_provider":"Cigna",
        "billing_amount":1500.00,
        "room_number":101,
        "admission_type":"Emergency",
        "created_at":"2023-10-01T10:00:00Z"
    }

    mocker.patch(
        "app.api.v1.encounters_router.service_get_encounter_by_id",
        return_value = fake_encounter,
    )

    response = client.get(f"/encounters/{fake_encounter['id']}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert data["id"] == str(fake_encounter["id"])
    assert data["doctor_name"] == "John Smith"

#------------------------------------------------------#
# Test for getting encounters by patient ID
#------------------------------------------------------#
def test_get_encounters_by_patient_id_returns_list_and_200(mocker):
    patient_id = uuid4()
    fake_encounters = [
        {"id": uuid4(),
         "patient_id": patient_id, 
         "admission_date": "2023-10-01", 
         "discharge_date": "2023-10-10", 
         "doctor_name":"John Smith", 
         "hospital_name":"General Hospital",
         "insurance_provider":"Cigna",
         "billing_amount":1500.00,
         "room_number":101,
         "admission_type":"Emergency",
         "created_at":"2023-10-01T10:00:00Z"},

         {"id": uuid4(),
          "patient_id": patient_id,
          "admission_date": "2023-11-05",
          "discharge_date": "2023-11-15",
          "doctor_name":"Emily Davis",
          "hospital_name":"City Medical Center",
          "insurance_provider":"Blue Cross",
          "billing_amount":2500.00,
          "room_number":202,
          "admission_type":"Elective",
          "created_at":"2023-11-05T14:30:00Z"},
    ]

    mocker.patch(
        "app.api.v1.encounters_router.service_get_encounters_by_patient_id",
        return_value = fake_encounters,
    )

    response = client.get(f"/encounters/by-patient/{patient_id}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["patient_id"] == str(patient_id)

#------------------------------------------------------#
# Test for getting encounters by hospital name
#------------------------------------------------------#
def test_get_encounters_by_hospital_name_returns_list_and_200(mocker):
    hospital_name = "General Hospital"
    fake_encounters = [
        {"id": uuid4(),
         "patient_id": uuid4(), 
         "admission_date": "2023-10-01", 
         "discharge_date": "2023-10-10", 
         "doctor_name":"John Smith", 
         "hospital_name":hospital_name,
         "insurance_provider":"Cigna",
         "billing_amount":1500.00,
         "room_number":101,
         "admission_type":"Emergency",
         "created_at":"2023-10-01T10:00:00Z"},

         {"id": uuid4(),
          "patient_id": uuid4(),
          "admission_date": "2023-11-05",
          "discharge_date": "2023-11-15",
          "doctor_name":"Emily Davis",
          "hospital_name":hospital_name,
          "insurance_provider":"Blue Cross",
          "billing_amount":2500.00,
          "room_number":202,
          "admission_type":"Elective",
          "created_at":"2023-11-05T14:30:00Z"},
    ]

    mocker.patch(
        "app.api.v1.encounters_router.service_get_encounters_by_hospital_name",
        return_value = fake_encounters,
    )

    response = client.get(f"/encounters/by-hospital/{hospital_name}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["hospital_name"] == hospital_name


#------------------------------------------------------#
# Test for getting encounters by doctor name
#------------------------------------------------------#

def test_get_encounters_by_doctor_name_returns_list_and_200(mocker):
    fake_doctor_name = "John Smith"
    fake_encounters = [
        {"id": uuid4(),
         "patient_id": uuid4(), 
         "admission_date": "2023-10-01", 
         "discharge_date": "2023-10-10", 
         "doctor_name":fake_doctor_name, 
         "hospital_name":"General Hospital",
         "insurance_provider":"Cigna",
         "billing_amount":1500.00,
         "room_number":101,
         "admission_type":"Emergency",
         "created_at":"2023-10-01T10:00:00Z"},

         {"id": uuid4(),
          "patient_id": uuid4(),
          "admission_date": "2023-11-05",
          "discharge_date": "2023-11-15",
          "doctor_name":fake_doctor_name,
          "hospital_name":"City Medical Center",
          "insurance_provider":"Blue Cross",
          "billing_amount":2500.00,
          "room_number":202,
          "admission_type":"Elective",
          "created_at":"2023-11-05T14:30:00Z"},
    ]

    mocker.patch(
        "app.api.v1.encounters_router.service_get_encounters_by_doctor_name",
        return_value = fake_encounters,
    )

    response = client.get(f"/encounters/by-doctor/{fake_doctor_name}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["doctor_name"] == fake_doctor_name