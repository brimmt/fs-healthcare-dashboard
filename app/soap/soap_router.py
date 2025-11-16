from fastapi import APIRouter, Response
import os


router = APIRouter(prefix="/soap", tags=["SOAP"])

BASE_PATH = os.path.join(os.path.dirname(__file__), "endpoints")

def load_xml(filename: str) -> str:
    file_path = os.path.join(BASE_PATH, filename)
    with open(file_path, "r") as f:
        return f.read()
    
@router.get("/GetPatients")
def get_patients():
    xml_data = load_xml("patients.xml")
    return Response(content=xml_data, media_type="applicaton/xml")


@router.get("/GetEncounters")
def get_encounters():
    xml_data = load_xml("encounters.xml")
    return Response(content=xml_data, media_type="application/xml")


@router.get("/GetConditions")
def get_conditions():
    xml_data = load_xml("conditions.xml")
    return Response(content=xml_data, media_type="application/xml")


@router.get("GetTestResults")
def get_test_results():
    xml_data = load_xml("test_results")
    return Response(content=xml_data, media_type="application/xml")



