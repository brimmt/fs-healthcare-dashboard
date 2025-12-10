"""Testing all Test Result Service Functions """

from uuid import uuid4

from app.services.test_result_service import (
    get_test_results_by_id,
    get_all_test_results,
    get_test_results_by_encounter_id,
)


# -------------------------------------------------------#
# Test get test result by id and returns none if test result not found
# -------------------------------------------------------#
def test_get_test_result_by_id_returns_none_for_missing_test_result(mocker):
    # Fake response object

    fake_response = mocker.Mock()
    fake_response.data = None

    # Mock execute() to return fake response
    mock_single = mocker.Mock()
    mock_single.execute.return_value = fake_response

    # Mock eq() to return mock_single
    mock_eq = mocker.Mock()
    mock_eq.single.return_value = mock_single

    # Mock select() to return mock_eq
    mock_select = mocker.Mock()
    mock_select.eq.return_value = mock_eq

    # Mock table() to return mock_select
    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    # Mock supabase client
    mocker.patch(
        "app.services.test_result_service.supabase.table", return_value=mock_table
    )

    # Run the function with a random UUID
    fake_id = uuid4()
    result = get_test_results_by_id(fake_id)

    assert result is None


# --------------------------------------------------------#
# Test get all test results returns list
# --------------------------------------------------------#
def test_get_all_test_results_returns_list(mocker):
    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "test_name": "Blood Test",
            "result": "Normal",
        },
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "test_name": "X-Ray",
            "result": "No Issues",
        },
    ]

    mock_execute = mocker.Mock()
    mock_execute.execute.return_value = fake_response

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_execute

    mocker.patch(
        "app.services.test_result_service.supabase.table", return_value=mock_table
    )

    result = get_all_test_results()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("test_name" in test_result for test_result in result)


# -------------------------------------------------------#
# Test get test result by encounter id returns list
# -------------------------------------------------------#


def test_get_test_results_by_encounter_id_returns_list(mocker):
    encounter_id = uuid4()

    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "encounter_id": str(encounter_id),
            "test_results": "Abnormal",
            "created_at": "2024-01-01T00:00:00Z",
        },
        {
            "id": str(uuid4()),
            "encounter_id": str(encounter_id),
            "test_results": "Normal",
            "created_at": "2024-01-01T00:00:00Z",
        },
    ]

    mock_eq = mocker.Mock()
    mock_eq.execute.return_value = fake_response

    mock_select = mocker.Mock()
    mock_select.eq.return_value = mock_eq

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch(
        "app.services.test_result_service.supabase.table", return_value=mock_table
    )
    result = get_test_results_by_encounter_id(encounter_id)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("encounter_id" in test_result for test_result in result)
    assert all(
        str(encounter_id) == test_result["encounter_id"] for test_result in result
    )
