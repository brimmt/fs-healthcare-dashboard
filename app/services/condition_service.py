from app.services.supabase_client import supabase
from uuid import UUID

CONDITION_TABLE = "condition"


def get_all_conditions():
    response = supabase.table(CONDITION_TABLE).select("*").execute()
    return response.data or []


# -------------------------------#
# Grab condition by ID
# -------------------------------#


def get_condition_by_id(condition_id: UUID):
    response = (
        supabase.table(CONDITION_TABLE)
        .select("*")
        .eq("id", str(condition_id))
        .single()
        .execute()
    )

    return response.data or None


# -------------------------------#
# Grab conditions by encounter ID
# -------------------------------#


def get_conditions_by_encounter_id(encounter_id: UUID):
    response = (
        supabase.table(CONDITION_TABLE)
        .select("*")
        .eq("encounter_id", str(encounter_id))
        .execute()
    )

    return response.data or []
