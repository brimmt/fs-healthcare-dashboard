from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date, datetime

class EncounterSchema(BaseModel):
    id: UUID
    patient_id: UUID
    admission_date: Optional[date]
    discharge_date: Optional[date]
    doctor_name: Optional[str]
    hospital_name: Optional[str]
    insurance_provider: Optional[str]
    billing_amount: Optional[float]
    room_number: Optional[int]
    admission_type: Optional[str]
    created_at: Optional[datetime] = None

