from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.schemas.test_result_schema import TestResultSchema
from app.services.test_result_service import get_all_test_results as service_get_all_test_results, get_test_results_by_id as service_get_test_results_by_id, get_test_results_by_encounter_id as service_get_test_results_by_encounter_id
from typing import List


router = APIRouter(prefix="/test-results", tags=["Test Results"])

#-------------------------------#
# Grab all test results 
#-------------------------------#

@router.get("/", response_model=List[TestResultSchema])
async def get_all_test_results():
    return service_get_all_test_results()


#-------------------------------#
# Grab test result by ID
#-------------------------------#

@router.get("/{test_result_id}", response_model=TestResultSchema)
async def get_test_results_by_id(test_result_id: UUID):
    result = service_get_test_results_by_id(test_result_id)

    if result is None:
        raise HTTPException(
            status_code=404, 
            detail="Test result not found"
            )
    return result


#-------------------------------#
# Grab test results by encounter ID
#-------------------------------#
@router.get("/by-encounter/{encounter_id}", response_model=List[TestResultSchema])
async def get_test_results_by_encounter_id(encounter_id: UUID):
    result = service_get_test_results_by_encounter_id(encounter_id)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404, 
            detail="No test results found for the specified encounter ID"
            )
    return result

