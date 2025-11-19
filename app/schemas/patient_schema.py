from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime
from schemas.encounter_schema import EncounterSchema

class PatientSchema(BaseModel):
    id: UUID
    patient_name: str
    age: int
    gender: str
    blood_type: str
    created_at: Optional[datetime] = None


class PatientDetailResponse(BaseModel):
    patient: PatientSchema
    encounters: List[EncounterSchema]