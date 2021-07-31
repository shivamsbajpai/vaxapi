from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.data import database
from app.schema.requests.userDetailsRequest import UserDetailsRequest
from app.services import userDetailsService

get_db = database.get_db


router = APIRouter(
    prefix="/user/create",
    tags=['Fill your details']
)



@router.post('/', status_code=status.HTTP_201_CREATED)
def user_create_rent_details(request: UserDetailsRequest, db: Session = Depends(get_db)):
    return userDetailsService.create_user_details(request, db)
