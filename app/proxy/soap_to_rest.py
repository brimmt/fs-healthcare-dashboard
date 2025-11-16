import requests
from app.soap.parser import parse_xml
from app.proxy.mappings import (
    map_patient_soap_to_rest,
    map_encounter_soap_to_rest
)

SOAP_BASE_URL = "http://127.0.0.1:8000/soap"


def fetch_soap_xml(endpoint: str) -> str:
    url = f"{SOAP_BASE_URL}/{endpoint}"
    response = requests.get(url)
    return response.text


def get_patients_from_soap():
    """
    Fetch SOAP Patients XML → parse → map → return REST-ready list.
    """
    xml = fetch_soap_xml("GetPatients")
    data = parse_xml(xml)

    raw_list = data["Patients"]["Patient"]
    results = [map_patient_soap_to_rest(p) for p in raw_list]

    return results


def get_encounters_from_soap():
    """
    Fetch SOAP Encounters XML → parse → map → return REST-ready list.
    """
    xml = fetch_soap_xml("GetEncounters")
    data = parse_xml(xml)

    raw_list = data["Encounters"]["Encounter"]
    results = [map_encounter_soap_to_rest(e) for e in raw_list]

    return results