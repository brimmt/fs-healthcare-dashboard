from app.services.supabase_client import supabase
from uuid import UUID


PATIENT_TABLE = "patient"
ENCOUNTER_TABLE = "encounter"

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

def get_patient_by_name(patient_name: str):
     response = (
          supabase.table(PATIENT_TABLE)
          .select('*')
          .eq('patient_name', str(patient_name))
          .limit(100)
          .execute()
     )

     return response.data



def get_patient_details(patient_id: UUID):
 
        patient_response = (
            supabase.table(PATIENT_TABLE)
            .select('*')
            .eq("id", str(patient_id))
            .single()
            .execute()
        )

        patient = patient_response.data
        if not patient:
            return None
        
        encounters_response = (
            supabase.table(ENCOUNTER_TABLE)
            .select("*")
            .eq("patient_id", str(patient_id))
            .execute()
        )

        encounters = encounters_response.data or []

       
        return {
            "patient": patient,
            "encounters": encounters
        }
   

