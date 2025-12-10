from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

client = OpenAI(api_key=OPENAI_API_KEY)


SYSTEM_MESSAGE = """ 
You are a clinical summarization assistant that helps healthcare professionals by providing concise summaries of patient data. 
Your task is to analyze the provided patient information, 
including demographics, medical history, medications, allergies, lab results, and clinical notes, 
and generate a clear and informative summary that highlights key health issues, recent changes in condition, 
and any critical alerts or recommendations for care.
If data is missing or incomplete, please indicate this in your summary. 
Do not make assumptions beyond the provided information.
"""

# Building the prompt for the AI model

def build_summary_prompt(patient_details: dict):
    patient = patient_details.get("patient", {})
    encounters = patient_details.get("encounters", [])
    conditions = patient_details.get("conditions", [])
    test_results = patient_details.get("test_results", [])
    medications = patient_details.get("medications", [])

    return f"""
PATIENT INFORMATION:
Name: {patient.get('patient_name', 'N/A')}
Age: {patient.get('age', 'N/A')}
Gender: {patient.get('gender', 'N/A')}
Blood Type: {patient.get('blood_type', 'N/A')}

ENCOUNTERS:
{encounters if encounters else 'No encounter data available.'}

CONDITIONS:
{conditions if conditions else 'No conditions data available.'}

MEDICATIONS:
{medications if medications else 'No medication data available.'}

TEST RESULTS:
{test_results if test_results else 'No test results available.'}

TASK:
Generate a clinically relevant patient summary using ONLY the data provided.
Highlight:
- key past medical history
- important encounters
- active conditions
- relevant labs/test patterns
- any risk factors
- missing or incomplete data

Do NOT hallucinate or assume information not explicitly provided.
"""



# Function to generate the client summary using OpenAI
def generate_client_summary(patient_details: dict) -> str:
    prompt = build_summary_prompt(patient_details)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": prompt},
        ],
        max_tokens=500,
        temperature=0.7,
    )

    summary_text = response.choices[0].message.content.strip()
    return summary_text