from app.services.supabase_client import supabase
from uuid import UUID

TEST_RESULT_TABLE = 'test_results'



def get_all_test_results():
    response = supabase.table(TEST_RESULT_TABLE).select('*').execute()
    return response.data


def get_test_results_by_id(test_result_id: UUID):
    response = (
        supabase.table(TEST_RESULT_TABLE)
        .select('*')
        .eq("id", str(test_result_id))
        .single()
        .execute()
    )

    return response.data