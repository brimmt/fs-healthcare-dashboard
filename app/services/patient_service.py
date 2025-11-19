from app.services.supabase_client import supabase
from uuid import UUID


PATIENT_TABLE = "patient"

def get_all_patients():
    response = supabase.table(PATIENT_TABLE).select('*').execute()
    return response.data


def get_patient_by_id(patient_id: UUID):
    response = (
        supabase.table(PATIENT_TABLE)
        .select('*')
        .eq("id", str(patient_id))
        .single()
        .execute()
    )

    return response.data



def