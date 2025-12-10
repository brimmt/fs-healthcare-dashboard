import strawberry
from typing import List, Optional
from uuid import UUID
from datetime import date, datetime


from app.services.patient_service import get_patient_details as service_get_patient_details


@strawberry.type
class ConditionType:
    id: UUID
    medical_condition: Optional[str]
    created_at: Optional[datetime]
    icd10_code: Optional[str]

@strawberry.type
class TestResultType:
    id: UUID
    test_results: Optional[str]
    created_at: Optional[datetime]

@strawberry.type
class EncounterType:
    id: UUID
    admission_date: Optional[date]
    discharge_date: Optional[date]
    doctor_name: Optional[str]
    hospital_name: Optional[str]
    insurance_provider: Optional[str]
    billing_amount: Optional[float]
    room_number: Optional[int]
    admission_type: Optional[str]
    created_at: Optional[datetime]
    conditions: List[ConditionType]
    test_results: List[TestResultType]


@strawberry.type
class PatientType:
    id: UUID
    patient_name: str
    age: int
    gender: str
    blood_type: str
    encounters: List[EncounterType]


@strawberry.type
class Query:
    @strawberry.field
    def patient_details(self, patient_id: UUID) -> Optional[PatientType]:
        data = service_get_patient_details(patient_id)
        if not data:
            return None


        patient = data['patient']
        encounters = data.get('encounters', [])

        # Construct EncounterType objects
        encounter_objects = [
            EncounterType(
                id=enc['id'],
                admission_date=enc.get('admission_date'),
                discharge_date=enc.get('discharge_date'),
                doctor_name=enc.get('doctor_name'),
                hospital_name=enc.get('hospital_name'),
                insurance_provider=enc.get('insurance_provider'),
                billing_amount=enc.get('billing_amount'),
                room_number=enc.get('room_number'),
                admission_type=enc.get('admission_type'),
                created_at=enc.get('created_at'),
                conditions=[
                    ConditionType(
                        id=cond['id'],
                        medical_condition=cond.get('medical_condition'),
                        created_at=cond.get('created_at'),
                        icd10_code=cond.get('icd10_code'),
                    )
                    for cond in enc.get('conditions', [])
                ],
                test_results=[
                    TestResultType(
                        id=tr['id'],
                        test_results=tr.get('test_results'),
                        created_at=tr.get('created_at'),
                    )
                    for tr in enc.get('test_results', [])
                ],
            )
            for enc in encounters
        ]

        # Construct and return PatientType object
        return PatientType(
            id=patient['id'],
            patient_name=patient['patient_name'],
            age=patient['age'],
            gender=patient['gender'],
            blood_type=patient['blood_type'],
            encounters=encounter_objects,
        )


schema = strawberry.Schema(query=Query)