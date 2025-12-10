def map_patient_soap_to_rest(patient_dict):
    return {
        "id": patient_dict.get("ID"),
        "name": patient_dict.get("Name"),
        "gender": patient_dict.get("Gender"),
        "dob": patient_dict.get("DOB")
    }


def map_encounter_soap_to_rest(enc_dict):
    diagnosis = enc_dict.get("Diagnosis", {})

    return {
        "encounter_id" : enc_dict.get("EncounterID"),
        "patient_id": enc_dict.get("PatientID"),
        "diagnosis_code": diagnosis.get("Code"),
        "diagnosis_description": diagnosis.get("Description"),
        "admission_type": enc_dict.get("AdmissionType"),
    }