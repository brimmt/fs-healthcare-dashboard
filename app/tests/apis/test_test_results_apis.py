''' Testing all Test Result API Routes'''

from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.test_results_router import router
from uuid import uuid4

app = FastAPI()
app.include_router(router)
client = TestClient(app)


#------------------------------------------------------#
# Test for getting all test results       
#------------------------------------------------------#
def test_get_all_test_results_returns_list_and_200(mocker):
    fake_test_results = [
        {"id": uuid4(),
         "encounter_id": uuid4(),  
         "test_results": "Normal", 
         "created_at":"2023-10-01T09:00:00Z"
         },

         {"id": uuid4(),
          "encounter_id": uuid4(),
          "test_results": "Elevated Cholesterol",
          "created_at":"2023-10-02T11:30:00Z"
         },
    ]

    mocker.patch(
        "app.api.v1.test_results_router.service_get_all_test_results",
        return_value = fake_test_results,
    )

    response = client.get("/test-results/")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    
#------------------------------------------------------#
# Test for getting test results by test result ID
#------------------------------------------------------#
def test_get_test_results_by_id_returns_test_result_and_200(mocker):
    fake_test_result = {
        "id": uuid4(),
        "encounter_id": uuid4(),
        "test_results": "Normal",
        "created_at":"2023-10-01T09:00:00Z"
    }

    mocker.patch(
        "app.api.v1.test_results_router.service_get_test_results_by_id",
        return_value = fake_test_result,
    )

    test_result_id = fake_test_result["id"]
    response = client.get(f"/test-results/{test_result_id}")
    data = response.json()

    # Assertions
    assert response.status_code == 200
    assert data["id"] == str(fake_test_result["id"])
    assert data["test_results"] == "Normal"