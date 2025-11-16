from app.services.supabase_client import supabase
from uuid import UUID

ENCOUNTER_TABLE = 'encounter'



def get_all_encounters():
    response = supabase.table(ENCOUNTER_TABLE).select('*').execute()
    return response.data


def get_encounter_by_id(encounter_id: UUID):
    response = (
        supabase.table(ENCOUNTER_TABLE)
        .select('*')
        .eq("id", str(encounter_id))
        .single()
        .execute()
    )

    return response.data