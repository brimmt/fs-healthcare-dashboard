from fastapi import APIRouter
from app.schemas.patient_schema import PatientSchema
from app.services.patient_service import get_all_patients as service_get_all_patients, get_patient_by_id as service_get_patient_by_id
from typing import List
from uuid import UUID

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/", response_model=List[PatientSchema])
async def get_all_patients():
    
    return service_get_all_patients()


@router.get("/{patient_id}", response_model=PatientSchema)
async def get_patient_by_id(patient_id: UUID):
   
    return service_get_patient_by_id(patient_id)

