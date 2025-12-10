from app.services.supabase_client import supabase
from uuid import UUID

ENCOUNTER_TABLE = 'encounter'

#-------------------------------#
# Grab all encounters   
#-------------------------------#

def get_all_encounters():
    response = supabase.table(ENCOUNTER_TABLE).select('*').execute()
    return response.data or []

#-------------------------------#
# Grab encounter by ID
#-------------------------------#
def get_encounter_by_id(encounter_id: UUID):
    response = (
        supabase.table(ENCOUNTER_TABLE)
        .select('*')
        .eq("id", str(encounter_id))
        .single()
        .execute()
    )

    return response.data or None

#-------------------------------#
# Grab encounter by patient ID
#-------------------------------#
def get_encounters_by_patient_id(patient_id: UUID):
    response = (
        supabase.table(ENCOUNTER_TABLE)
        .select('*')
        .eq("patient_id", str(patient_id))
        .execute()
    )

    return response.data or []


#------------------------------#
# Grab encounters by hopsital name
#------------------------------#
def get_encounters_by_hospital_name(hospital_name: str):
    response = (
        supabase.table(ENCOUNTER_TABLE)
        .select('*')
        .ilike('hospital_name', f"%{hospital_name}%")
        .limit(100) 
        .execute()
    )

    return response.data or []


#------------------------------#
# Grab encounters by doctor name
#------------------------------#

def get_encounters_by_doctor_name(doctor_name: str):
    response = (
        supabase.table(ENCOUNTER_TABLE)
        .select('*')
        .ilike('doctor_name', f"%{doctor_name}%")
        .limit(100) 
        .execute()
    )

    return response.data or None