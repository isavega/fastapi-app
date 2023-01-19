from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.model import ApplicantSchema

router = APIRouter()

applicants = {
    "1": {
        "name": "Isabel Vega",
        "linkedinProfile": "https://www.linkedin.com/in/isabelvegavillablanca/"
    },
}


@router.get("/")
def get_applicants() -> dict:
    return {
        "data": applicants
    }

@router.get("/{id}")
async def get_applicant(id: str) -> dict:
    if int(id) > len(applicants):
        return {
            "error": "Invalid applicant ID"
        }

    for applicant in applicants.keys():
        if applicant == id:
            return {
                "data": applicants[applicant]
            }

    return {
        "Error": "Invalid ID"
    }

@router.post("/")
def add_applicant(applicant: ApplicantSchema = Body(...)) -> dict:
    applicants[str(len(applicants)+1)] = applicant.dict()

    return {
        "message": "Bienvenido a Tenpo Lab! Puedes subir tu CV en este link: https://forms.gle/6Q5Z7Z7Z7Z7Z7Z7Z7"
    }

@router.put("/{id}")
def update_applicant(id: str, applicant: ApplicantSchema):
    stored_applicant = applicants[id]
    if stored_applicant:
        stored_applicant_model = ApplicantSchema(**stored_applicant)
        update_data = applicant.dict(exclude_unset=True)
        updated_applicant = stored_applicant_model.copy(update=update_data)
        applicants[id] = jsonable_encoder(updated_applicant)
        return {
            "message": "applicant updated successfully"
        }
    return {
        "error": "No such applicant exist"
    }

@router.delete("/{id}")
def delete_applicant(id: str) -> dict:
    if int(id) > len(applicants):
        return {
            "error": "Invalid applicant ID"
        }

    for applicant in applicants.keys():
        if applicant == id:
            del applicants[applicant]
            return {
                "message": "applicant deleted"
            }

    return {
        "error": "applicant with {} doesn't exist".format(id)
    }

