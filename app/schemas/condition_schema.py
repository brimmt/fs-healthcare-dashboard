from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class ConditionSchema(BaseModel):
    id: UUID
    encounter_id: UUID
    medical_condition: str
    icd10_code: str
    created_at: Optional[datetime] = None

