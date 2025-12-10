from fastapi import APIRouter, HTTPException
from uuid import UUID
from typing import List
from app.schemas.encounter_schema import EncounterSchema
from app.services.encounter_service import (
    get_all_encounters as service_get_all_encounters,
    get_encounter_by_id as service_get_encounter_by_id,
    get_encounters_by_patient_id as service_get_encounters_by_patient_id,
    get_encounters_by_hospital_name as service_get_encounters_by_hospital_name,
    get_encounters_by_doctor_name as service_get_encounters_by_doctor_name,
)


router = APIRouter(prefix="/encounters", tags=["Encounters"])

# -------------------------------#
# Grab all encounters
# -------------------------------#


@router.get("/", response_model=List[EncounterSchema])
async def get_all_encounters():

    return service_get_all_encounters()


# -------------------------------#
# Grab encounter by ID
# -------------------------------#


@router.get("/{encounter_id}", response_model=EncounterSchema)
async def get_encounter_by_id(encounter_id: UUID):
    result = service_get_encounter_by_id(encounter_id)

    if result is None or len(result) == 0:
        raise HTTPException(status_code=404, detail="Encounter not found")
    return result


# -------------------------------#
# Grab encounters by patient ID
# -------------------------------#


@router.get("/by-patient/{patient_id}", response_model=List[EncounterSchema])
async def get_encounters_by_patient_id(patient_id: UUID):
    result = service_get_encounters_by_patient_id(patient_id)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404, detail="No encounters found for the specified patient ID"
        )
    return result


# ------------------------------#
# Grab encounters by hospital name
# ------------------------------#


@router.get("/by-hospital/{hospital_name}", response_model=List[EncounterSchema])
async def get_encounters_by_hospital_name(hospital_name: str):
    result = service_get_encounters_by_hospital_name(hospital_name)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404,
            detail="No encounters found for the specified hospital name",
        )

    return result


# ------------------------------#
# Grab encounters by doctor name
# ------------------------------#


@router.get("/by-doctor/{doctor_name}", response_model=List[EncounterSchema])
async def get_encounters_by_doctor_name(doctor_name: str):
    result = service_get_encounters_by_doctor_name(doctor_name)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404, detail="No encounters found for the specified doctor name"
        )
    return result
