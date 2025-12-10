from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class TestResultSchema(BaseModel):
    id: UUID
    encounter_id: UUID
    test_results: str
    created_at: Optional[datetime] = None
