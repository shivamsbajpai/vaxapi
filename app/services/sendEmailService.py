from app.models.userDetails import UserDetails
import smtplib
import os
from email.message import EmailMessage
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.data.database import engine, Base
from app.data import database
import app.common.config as config


def email_body(response_list: list):
    response_string = ""
    for response in response_list:
        response_string += "Details\n"
        response_string += response
        response_string += "\n\n\n"
    return response_string



def send_multiple_email(recipients, subject: str, body: str):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    sender_email_id = os.environ.get("sender_email_id")
    sender_email_id_password = os.environ.get("sender_email_id_password")

    s.login(sender_email_id, sender_email_id_password)

    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = sender_email_id
    message['To'] = ', '.join(recipients)
    s.send_message(message)
    s.quit()


def get_email_ids(id):
    email145 = []
    email118 = []
    email245 = []
    email218 = []

    for user in config.user_details:
        if user.dose_number == 1 and user.age == 45:
            email145.append(user.email)
        elif user.dose_number == 1 and user.age == 18:
            email118.append(user.email)
        elif user.dose_number == 2 and user.age == 45:
            email245.append(user.email)
        elif user.dose_number == 2 and user.age == 18:
            email218.append(user.email)

    if(id == 145):
        return email145
    elif(id == 118):
        return email118
    elif(id == 245):
        return email245
    elif(id==218):
        return email218



