from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.patients_router import router
from uuid import uuid4
app = FastAPI()
app.include_router(router)



client = TestClient(app)

#------------------------------------------------------#
# Test for getting all patients
#------------------------------------------------------#

def test_get_all_patients_returns_list_and_200(mocker):
    # Fake what the resposne is suppose to look like
    fake_patients = [
        {"id": uuid4(), "patient_name": "John Doe", "age": 30, "gender": "Male", "blood_type": "O+"},
        {"id": uuid4(), "patient_name": "Jane Smith", "age": 25, "gender": "Female", "blood_type": "A-"},
    ]

    # Mock the supabase client to return the fake patients
    mocker.patch(
        "app.api.v1.patients_router.service_get_all_patients",
        return_value=fake_patients,
    )

    response = client.get("/patients")
    data = response.json()
    
     # Assertions
    
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["patient_name"] == "John Doe"
    assert data[1]["patient_name"] == "Jane Smith"
    

#------------------------------------------------------#
# Test for getting patients by name
#------------------------------------------------------#

def test_get_patient_by_name_returns_list_and_200(mocker):
    # Fake what the response is supposed to look like
    fake_patients = [
        {"id": uuid4(), "patient_name": "John Doe", "age": 30, "gender": "Male","blood_type": "O+"},
        {"id": uuid4(), "patient_name": "Johnny Appleseed", "age": 28, "gender":"Male","blood_type":"AB-"},
    ]

    mocker.patch(
        "app.api.v1.patients_router.service_get_patients_by_name",
        return_value = fake_patients,
    )
    response = client.get("/patients/by-name/John")
    data = response.json()


    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["patient_name"] == "John Doe"
    assert data[1]["patient_name"] == "Johnny Appleseed"


#------------------------------------------------------#
# Test for getting patient by ID
#------------------------------------------------------#

def test_get_patient_by_id_returns_patient_and_200(mocker):
    fake_paitent = {
        "id":uuid4(),
        "patient_name":"Alice Johnson",
        "age":40,
        "gender": "Female",
        "blood_type": "B+",
    }

    mocker.patch(
        "app.api.v1.patients_router.service_get_patient_by_id",
        return_value = fake_paitent,
    )

    response = client.get(f"/patients/{fake_paitent['id']}")
    data = response.json()


    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data["patient_name"] == "Alice Johnson"
    assert data["age"] == 40
    assert data["gender"] == "Female"
    assert data["blood_type"] == "B+"


#------------------------------------------------------#
# Test for getting patient details by ID
#------------------------------------------------------#

def test_get_patient_details_returns_details_and_200(mocker):
    fake_patient_id = uuid4()
    fake_details = {
  "patient": {
    "id": "7d775cd1-707f-4374-978d-ecbfd1558a6b",
    "patient_name": "John Doe",
    "age": 37,
    "gender": "Male",
    "blood_type": "A-",
    "created_at": "2025-11-15T21:12:45.409826"
  },
  "encounters": [
    {
      "id": "b54848fe-21e9-4f66-9218-8c9cb0116be3",
      "patient_id": "7d775cd1-707f-4374-978d-ecbfd1558a6b",
      "admission_date": "2020-03-05",
      "discharge_date": "2020-03-21",
      "doctor_name": "Carol Reed",
      "hospital_name": "Hughes Cowan Bell",
      "insurance_provider": "Aetna",
      "billing_amount": 23807.56,
      "room_number": 231,
      "admission_type": "Elective",
      "created_at": "null",
      "conditions": [
        {
          "id": "8a260897-a0c6-45f7-b0ea-2a552dd617c0",
          "encounter_id": "b54848fe-21e9-4f66-9218-8c9cb0116be3",
          "medical_condition": "Cancer",
          "created_at": "2025-11-15T21:24:42.42018",
          "icd10_code": "C80.1"
        }
      ],
      "test_results": [
        {
          "id": "6253c24a-c97b-4c36-8696-18b866c16bbe",
          "encounter_id": "b54848fe-21e9-4f66-9218-8c9cb0116be3",
          "test_results": "Abnormal",
          "created_at": "2025-11-15T21:26:55.261793"
        }
      ]
    }
  ]
}
    
    mocker.patch(
        "app.api.v1.patients_router.service_get_patient_details",
        return_value = fake_details,
    )

    response = client.get(f"/patients/{fake_patient_id}/details")
    data = response.json()


    assert response.status_code == 200
    assert isinstance(data, dict)
    assert data["patient"]["patient_name"] == "John Doe"
    assert len(data["encounters"]) == 1
    assert data["encounters"][0]["doctor_name"] == "Carol Reed"

    
