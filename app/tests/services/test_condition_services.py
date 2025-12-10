""" Testing all Conditions Service Functions """

import pytest
from uuid import uuid4

from app.services.condition_service import (
    get_condition_by_id,
    get_all_conditions,
    get_conditions_by_encounter_id,
)


# -------------------------------------------------------#
# Test get condition by id and returns none if condition not found
# -------------------------------------------------------#
def test_get_condition_by_id_returns_none_for_missing_condition(mocker):
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
        "app.services.condition_service.supabase.table", return_value=mock_table
    )

    # Run the function with a random UUID
    fake_id = uuid4()
    result = get_condition_by_id(fake_id)

    assert result is None


# -------------------------------------------------------#
# Test get all conditions returns list
# -------------------------------------------------------#
def test_get_all_conditions_returns_list(mocker):
    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "condition_name": "Hypertension",
            "severity": "High",
        },
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "condition_name": "Diabetes",
            "severity": "Medium",
        },
    ]

    mock_select = mocker.Mock()
    mock_select.execute.return_value = fake_response

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch(
        "app.services.condition_service.supabase.table", return_value=mock_table
    )

    result = get_all_conditions()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("condition_name" in condition for condition in result)


# -------------------------------------------------------#
# Test get conditions by encounter id returns list
# -------------------------------------------------------#
def test_get_conditions_by_encounter_id_returns_list(mocker):
    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "condition_name": "Asthma",
            "severity": "Low",
        },
        {
            "id": str(uuid4()),
            "encounter_id": str(uuid4()),
            "condition_name": "Allergy",
            "severity": "Medium",
        },
    ]

    mock_select = mocker.Mock()
    mock_select.execute.return_value = fake_response

    mock_eq = mocker.Mock()
    mock_eq.eq.return_value = mock_select

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_eq

    mocker.patch(
        "app.services.condition_service.supabase.table", return_value=mock_table
    )

    result = get_conditions_by_encounter_id(uuid4)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("encounter_id" in condition for condition in result)
