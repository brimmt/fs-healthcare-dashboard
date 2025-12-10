""" Testing all Patient Service functions """

import pytest
from uuid import uuid4
from app.services.patient_service import (
    get_patient_by_id,
    get_all_patients,
    get_patient_by_name,
    get_patient_details,
)


# -------------------------------------------------------#
# Test get patient by id amd returns none if pateint not found
# -------------------------------------------------------#
def test_get_patient_by_id_returns_none_for_missing_patient(mocker):
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
    mocker.patch("app.services.patient_service.supabase.table", return_value=mock_table)

    # Run the function with a random UUID
    fake_id = uuid4()
    result = get_patient_by_id(fake_id)

    assert result is None


# -------------------------------------------------------#
# Test get all patients returns list of patients
# -------------------------------------------------------#
def test_get_all_patients_returns_list_of_patients(mocker):
    fake_patients = [
        {
            "id": uuid4(),
            "patient_name": "Alice Johnson",
            "age": 40,
            "gender": "Female",
            "blood_type": "B+",
        },
        {
            "id": uuid4(),
            "patient_name": "Bob Smith",
            "age": 35,
            "gender": "Male",
            "blood_type": "A-",
        },
    ]

    mock_select = mocker.Mock()
    mock_select.execute.return_value = mocker.Mock(data=fake_patients)

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_select

    mocker.patch("app.services.patient_service.supabase.table", return_value=mock_table)
    result = get_all_patients()

    assert isinstance(result, list)
    assert len(result) == 2


# -------------------------------------------------------#
# Test get patient by name returns list of patients
# ------------------------------------------------------#
def test_patient_by_name_returns_list_of_patients(mocker):
    fake_patients = [
        {
            "id": uuid4(),
            "patient_name": "Alice Johnson",
            "age": 30,
            "gender": "Female",
            "blood_type": "B+",
        },
        {
            "id": uuid4(),
            "patient_name": "Alicia Keys",
            "age": 28,
            "gender": "Female",
            "blood_type": "O-",
        },
    ]

    mock_select = mocker.Mock()
    mock_select.execute.return_value = mocker.Mock(data=fake_patients)

    mock_ilike = mocker.Mock()
    mock_ilike.limit.return_value = mock_select

    mock_limit = mocker.Mock()
    mock_limit.ilike.return_value = mock_ilike

    mock_table = mocker.Mock()
    mock_table.select.return_value = mock_limit

    mocker.patch("app.services.patient_service.supabase.table", return_value=mock_table)
    result = get_patient_by_name("Alic")

    assert isinstance(result, list)
    assert len(result) == 2
    assert all("Alic" in patient["patient_name"] for patient in result)


# -------------------------------------------------------#
# Test get patient details returns none for missing patient
# -------------------------------------------------------#
def test_get_patient_details_returns_none_for_missing_patient(mocker):
    # Fake response for patient not found
    fake_patient_response = mocker.Mock()
    fake_patient_response.data = None

    # Mock execute() to return fake patient response
    mock_single = mocker.Mock()
    mock_single.execute.return_value = fake_patient_response

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
    mocker.patch("app.services.patient_service.supabase.table", return_value=mock_table)

    # Run the function with a random UUID
    fake_id = uuid4()
    result = get_patient_details(fake_id)

    assert result is None
