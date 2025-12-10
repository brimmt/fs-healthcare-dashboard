""" Testing all Encounter Service Functions """

import pytest
from uuid import uuid4

from pytest_mock import mocker
from app.services.encounter_service import (
    get_encounter_by_id,
    get_all_encounters,
    get_encounters_by_patient_id,
    get_encounters_by_hospital_name,
    get_encounters_by_doctor_name,
)


# -------------------------------------------------------#
# Test get encounter by id and returns none if encounter not found
# -------------------------------------------------------#
def test_get_encounter_by_id_returns_none_for_missing_encounter(mocker):
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
        "app.services.encounter_service.supabase.table", return_value=mock_table
    )

    # Run the function with a random UUID
    fake_id = uuid4()
    result = get_encounter_by_id(fake_id)

    assert result is None


# -------------------------------------------------------#
# Test get all encounters returns list
# -------------------------------------------------------#
def test_get_all_encounters_returns_list(mocker):
    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "General Hospital",
            "doctor_name": "Dr. Smith",
        },
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "City Clinic",
            "doctor_name": "Dr. Jones",
        },
    ]

    # Mock execute() to return fake response
    mock_execute = mocker.Mock()
    mock_execute.execute.return_value = fake_response

    # Mock select() to return mock_execute
    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_execute

    # Mock supabase client
    mocker.patch(
        "app.services.encounter_service.supabase.table", return_value=mock_table
    )

    # Run the function
    result = get_all_encounters()

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("hospital_name" in encounter for encounter in result)


# -------------------------------------------------------#
# Test get encounters by patient id returns list
# -------------------------------------------------------#
def test_get_encounters_by_patient_id_returns_list(mocker):
    patient_id = uuid4()

    # Fake response object
    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "patient_id": str(patient_id),
            "hospital_name": "General Hospital",
            "doctor_name": "Dr. Smith",
        },
        {
            "id": str(uuid4()),
            "patient_id": str(patient_id),
            "hospital_name": "City Clinic",
            "doctor_name": "Dr. Jones",
        },
    ]

    mock_eq = mocker.Mock()
    mock_eq.execute.return_value = fake_response

    mock_select = mocker.Mock()
    mock_select.eq.return_value = mock_eq

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch(
        "app.services.encounter_service.supabase.table", return_value=mock_table
    )
    result = get_encounters_by_patient_id(patient_id)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(str(patient_id) == encounter["patient_id"] for encounter in result)


# -------------------------------------------------------#
# Test get encounters by hospital name returns list
# -------------------------------------------------------#
def test_get_encounters_by_hospital_name_returns_list(mocker):
    hospital_name = "General"

    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "General Hospital",
            "doctor_name": "Dr. Smith",
        },
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "General Health Center",
            "doctor_name": "Dr. Jones",
        },
    ]

    mock_limit = mocker.Mock()
    mock_limit.execute.return_value = fake_response

    mock_ilike = mocker.Mock()
    mock_ilike.limit.return_value = mock_limit

    mock_select = mocker.Mock()
    mock_select.ilike.return_value = mock_ilike

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch(
        "app.services.encounter_service.supabase.table", return_value=mock_table
    )
    result = get_encounters_by_hospital_name(hospital_name)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(hospital_name in encounter["hospital_name"] for encounter in result)


# -------------------------------------------------------#
# Test get encounters by doctor name returns list
# -------------------------------------------------------#
def test_get_encounters_by_doctor_name_returns_list(mocker):
    doctor_name = "John Doe"

    fake_response = mocker.Mock()
    fake_response.data = [
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "General Hospital",
            "doctor_name": doctor_name,
        },
        {
            "id": str(uuid4()),
            "patient_id": str(uuid4()),
            "hospital_name": "City Clinic",
            "doctor_name": doctor_name,
        },
    ]

    mock_limit = mocker.Mock()
    mock_limit.execute.return_value = fake_response

    mock_ilike = mocker.Mock()
    mock_ilike.limit.return_value = mock_limit

    mock_select = mocker.Mock()
    mock_select.ilike.return_value = mock_ilike

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch(
        "app.services.encounter_service.supabase.table", return_value=mock_table
    )
    result = get_encounters_by_doctor_name(doctor_name)

    assert isinstance(result, list)
    assert len(result) == 2
    assert all(doctor_name in encounter["doctor_name"] for encounter in result)
