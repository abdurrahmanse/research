from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Root endpoint


@app.get("/")
def read_root():
    return {"Hello": "Patient Management API"}

# About endpoint


@app.get("/about")
def about():
    return {"About": "This API is designed to manage patient records, appointments, and medical history. It provides endpoints for creating, reading, updating, and deleting patient information."}

# Endpoint to get all patients


@app.get("/patients")
def get_patients(description: str = Path(..., description="Description of the patients to retrieve", example="All patients with diabetes")):
    data = load_data()
    return data

# Endpoint to get a specific patient by ID


@app.get("/patients/{patient_id}")
def get_patient(patient_id: str = Path(..., description="ID of the patient to retrieve", example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# Endpoint to sort patients by a specific field (e.g., height, weight, age)


@app.get("/patients/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Field to sort patients by (e.g., height, weight, age)",
        example="age")):
    field = sort_by.lower()
    order: str = Query(
        "asc",
        description="Order to sort patients by (e.g., asc, desc)",
        example="asc"
    )
    valid_fields = {"height", "weight", "age"}
    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")

    if order not in {"asc", "desc"}:
        raise HTTPException(
            status_code=400, detail="Invalid sort order Valid orders are: asc, desc")

    data = load_data()

    sort_reverse = True if order == "desc" else False

    sorted_patients = sorted(data.values(), key=lambda x: x.get(
        sort_by, 0), reverse=sort_reverse)
    return sorted_patients
