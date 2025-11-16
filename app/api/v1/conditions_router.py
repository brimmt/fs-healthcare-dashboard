from fastapi import APIRouter
from uuid import UUID
from app.schemas.condition_schema import ConditionSchema
from app.services.condition_service import get_all_conditions as service_get_all_conditions, get_condition_by_id as service_get_condition_by_id
from typing import List


router = APIRouter(prefix="/conditions", tags=["Conditions"])



@router.get("/", response_model=List[ConditionSchema])
async def get_all_conditions():
    return service_get_all_conditions()



@router.get("/{condition_id}", response_model=ConditionSchema)
async def get_condition_by_id(condition_id: UUID):

    return service_get_condition_by_id(condition_id)