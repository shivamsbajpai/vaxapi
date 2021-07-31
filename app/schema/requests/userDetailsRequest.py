import re
from pydantic import BaseModel,validator

class UserDetailsRequest(BaseModel):
    email: str
    dose_number: int
    district_code: int
    age: int
    whatsappNumber: str

    @validator("age")
    def age_validation(cls, v):
        if not (v == 18 or v == 45):
            raise ValueError('Please pass 18 or 45 as age')
        return v
    
    @validator("whatsappNumber")
    def whatsapp_validation(cls, v):
        if not bool(re.search("^\\+[1-9]\\d{1,14}$", v)):
            raise ValueError('Invalid phone number')
        if not len(v) == 13:
            raise ValueError('Length of phone number should be 10')
        return v

    @validator("district_code")
    def district_code_validation(cls, v):
        if v != 664:
            raise ValueError('Please pass 664 for Kanpur Nagar')
        return v

    @validator("dose_number")
    def dose_number_validation(cls, v):
        if not (v == 1 or v==2):
            raise ValueError('Please pass 1 or 2 as dose_number')
        return v
