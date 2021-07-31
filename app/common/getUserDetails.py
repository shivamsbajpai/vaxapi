from app.models.userDetails import UserDetails
import smtplib
import os
from email.message import EmailMessage
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.data.database import engine, Base
from app.data import database

get_db = database.get_db
db: Session = Depends(get_db)
session = Session(engine)

def get_user_details():
    user_details = session.query(UserDetails).all()
    return user_details

