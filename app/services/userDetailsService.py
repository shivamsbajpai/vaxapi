from sqlalchemy.orm import Session
from app.models.userDetails import UserDetails
from app.schema.requests.userDetailsRequest import UserDetailsRequest



def create_user_details(request: UserDetailsRequest, db: Session):
    userDetails = UserDetails(**request.dict())
    db.add(userDetails)
    db.commit()
    db.refresh(userDetails)
    return "Success! You will recieve notifications in your email"