from fastapi import APIRouter, HTTPException
from uuid import UUID
from app.schemas.condition_schema import ConditionSchema
from app.services.condition_service import (
    get_all_conditions as service_get_all_conditions,
    get_condition_by_id as service_get_condition_by_id,
    get_conditions_by_encounter_id as service_get_conditions_by_encounter_id,
)
from typing import List


router = APIRouter(prefix="/conditions", tags=["Conditions"])


# -------------------------------#
# Grab all conditions
# -------------------------------#


@router.get("/", response_model=List[ConditionSchema])
async def get_all_conditions():
    return service_get_all_conditions()


# -------------------------------#
# Grab condition by ID
# -------------------------------#


@router.get("/{condition_id}", response_model=ConditionSchema)
async def get_condition_by_id(condition_id: UUID):
    result = service_get_condition_by_id(condition_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Condition not found")
    return result


# -------------------------------#
# Grab conditions by encounter ID
# -------------------------------#
@router.get("/by-encounter/{encounter_id}", response_model=List[ConditionSchema])
async def get_conditions_by_encounter_id(encounter_id: UUID):
    result = service_get_conditions_by_encounter_id(encounter_id)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404, detail="No conditions found for the specified encounter ID"
        )
    return result
