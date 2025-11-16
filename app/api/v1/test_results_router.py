from fastapi import APIRouter
from uuid import UUID
from app.schemas.test_result_schema import TestResultSchema
from app.services.test_result_service import get_all_test_results as service_get_all_test_results, get_test_results_by_id as service_get_test_results_by_id
from typing import List


router = APIRouter(prefix="/test-results", tags=["Test Results"])


@router.get("/", response_model=List[TestResultSchema])
async def get_all_test_results():
    return service_get_all_test_results()



@router.get("/{test_result_id}", response_model=TestResultSchema)
async def get_test_results_by_id(test_result_id: UUID):

    return service_get_test_results_by_id(test_result_id)