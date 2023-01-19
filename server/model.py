from typing import Optional

from pydantic import BaseModel

class ApplicantSchema(BaseModel):
    name: Optional[str]
    linkedinProfile: Optional[str]

