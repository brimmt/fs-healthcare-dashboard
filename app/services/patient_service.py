from app.services.supabase_client import supabase
from uuid import UUID


PATIENT_TABLE = "patient"
ENCOUNTER_TABLE = "encounter"
CONDITION_TABLE = "condition"
TEST_RESULT_TABLE = "test_results"

#-------------------------------#
# Grab all patients   
#-------------------------------#

def get_all_patients():
    response = supabase.table(PATIENT_TABLE).select('*').execute()
    return response.data or []

#-------------------------------#
# Grab patient by ID
#-------------------------------#


def get_patient_by_id(patient_id: UUID):
    response = (
        supabase.table(PATIENT_TABLE)
        .select('*')
        .eq("id", str(patient_id))
        .single()
        .execute()
    )

    return response.data or None


#-------------------------------#
# Grab patients by name 
#-------------------------------#

def get_patient_by_name(patient_name: str):
     response = (
          supabase.table(PATIENT_TABLE)
          .select('*')
          .ilike('patient_name', f"%{patient_name}%")
          .limit(100)
          .execute()
     )

     return response.data or []

#-------------------------------#
# Grab patient details using patient ID
#-------------------------------#

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


        for encounter in encounters:
            conditions_response = (
                supabase.table(CONDITION_TABLE)
                .select("*")
                .eq("encounter_id", str(encounter["id"]))
                .execute()
            )
            encounter["conditions"] = conditions_response.data or []

            test_results_response = (
                supabase.table(TEST_RESULT_TABLE)
                .select("*")
                .eq("encounter_id", str(encounter["id"]))
                .execute()
            )
            encounter["test_results"] = test_results_response.data or []

       
        return {
            "patient": patient,
            "encounters": encounters
        }
        


   

