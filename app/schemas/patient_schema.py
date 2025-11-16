from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class PatientSchema(BaseModel):
    id: UUID
    patient_name: str
    age: int
    gender: str
    blood_type: str
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True