from fastapi import APIRouter, HTTPException
from app.schemas.patient_schema import PatientSchema
from app.services.patient_service import get_all_patients as service_get_all_patients, get_patient_by_id as service_get_patient_by_id, get_patient_details as service_get_patient_details, get_patient_by_name as service_get_patients_by_name
from app.services.ai_services.client_summary import generate_client_summary
from typing import List
from uuid import UUID

# Define the API router for patients
router = APIRouter(prefix="/patients", tags=["Patients"])

# Grab all patients
@router.get("/", response_model=List[PatientSchema])
async def get_all_patients():
    
    return service_get_all_patients()

# Grab patients by name
@router.get("/by-name/{patient_name}", response_model=List[PatientSchema])
async def get_patients_by_name(patient_name: str):
    result = service_get_patients_by_name(patient_name)

    if result is None or len(result) == 0:
        raise HTTPException(
            status_code=404, 
            detail="No patients found for the specified name"
            )
    return result

# Grab patient by ID
@router.get("/{patient_id}", response_model=PatientSchema)
async def get_patient_by_id(patient_id: UUID):
    result = service_get_patient_by_id(patient_id)

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )
    return result

# Grab patient details using patient ID
@router.get("/{patient_id}/details")
async def get_patient_details(patient_id: UUID):
    result = service_get_patient_details(patient_id)

    if result is None or not result.get("patient"):
        raise HTTPException(
            status_code=404,
            detail="Patient details not found"
        )
    return result


# Generate AI-powered patient summary
@router.get("/{patient_id}/summary")
async def get_patient_summary(patient_id: UUID):
    details = service_get_patient_details(patient_id)

    if not details or not details.get("patient"):
        raise HTTPException(status_code=404, detail="Patient not found")

    summary = generate_client_summary(details)
    return {"summary": summary}

