from fastapi import APIRouter
from uuid import UUID
from typing import List
from app.schemas.encounter_schema import EncounterSchema
from app.services.encounter_service import get_all_encounters as service_get_all_encounters, get_encounter_by_id as service_get_encounter_by_id


router = APIRouter(prefix="/encounters", tags=["Encounters"])


@router.get("/", response_model=List[EncounterSchema])
async def get_all_encounters():

    return service_get_all_encounters()


@router.get("/{encounter_id}", response_model=EncounterSchema)
async def get_encounter_by_id(encounter_id: UUID):


    return service_get_encounter_by_id(encounter_id)





