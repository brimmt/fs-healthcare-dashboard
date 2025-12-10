from app.services.supabase_client import supabase
from uuid import UUID

TEST_RESULT_TABLE = "test_results"


# -------------------------------#
# Grab all test results
# -------------------------------#


def get_all_test_results():
    response = supabase.table(TEST_RESULT_TABLE).select("*").execute()
    return response.data or []


# -------------------------------#
# Grab test result by ID
# -------------------------------#


def get_test_results_by_id(test_result_id: UUID):
    response = (
        supabase.table(TEST_RESULT_TABLE)
        .select("*")
        .eq("id", str(test_result_id))
        .single()
        .execute()
    )

    return response.data or None


# -------------------------------#
# Grab test results by encounter ID
# -------------------------------#


def get_test_results_by_encounter_id(encounter_id: UUID):
    response = (
        supabase.table(TEST_RESULT_TABLE)
        .select("*")
        .eq("encounter_id", str(encounter_id))
        .execute()
    )

    return response.data or []
