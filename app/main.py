from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.soap.soap_router import router as soap_router
from app.proxy.soap_to_rest import get_patients_from_soap

from app.api.v1.patients_router import router as patients_router
from app.api.v1.encounters_router import router as encounters_router
from app.api.v1.conditions_router import router as conditions_router
from app.api.v1.test_results_router import router as test_results_router
from app.graphql.router import router as graphql_router


app = FastAPI(title="Healthcare Modernization API",
              version="1.0.0",
              description="SOAP -> Proxy -> Rest -> FastAPI backend with Supabase")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #Tati <-- dont forget to change this after testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



#Routers

app.include_router(soap_router)
app.include_router(patients_router)
app.include_router(encounters_router)
app.include_router(conditions_router)
app.include_router(test_results_router)
app.include_router(graphql_router)


@app.get("/")
async def root():
    return {"message": "Healthcare API is running!"}


@app.get("/debug/patients-from-soap")
def debug():
    return get_patients_from_soap()