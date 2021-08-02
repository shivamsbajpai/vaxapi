from app.services import sendEmailService
import requests
import json
from app.data import database
from types import SimpleNamespace as Namespace
from datetime import datetime,timedelta

get_db = database.get_db


def api_call(district_id,date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
    #district_id = 664
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'district_id': district_id, 'date': date}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    data_string = str(r.text)

    x = json.loads(data_string, object_hook=lambda d: Namespace(**d))

    response_list = list()
    for vaccine_details in x.sessions:
        if vaccine_details.min_age_limit >= 18 and (vaccine_details.available_capacity_dose1 > 0 or vaccine_details.available_capacity_dose2 > 0) :
            response_list.append(vaccine_details)
    
    if len(response_list) != 0:
        create_responses(date,response_list)



def find_vaccine_slot():
    today = datetime.today() + timedelta(0)
    today_date = today.strftime('%d-%m-%Y')

    tomorrow = datetime.today() + timedelta(1)
    tomorrow_date = tomorrow.strftime('%d-%m-%Y')
    api_call(664,today_date)
    api_call(664,tomorrow_date)


def create_responses(date,response_list: list):
    dose145 = list()
    dose118 = list()
    dose245 = list()
    dose218 = list()
    for response in response_list:
        if(response.available_capacity_dose1 > 0 and response.min_age_limit >= 45):
            res145 = create_response_string(date,response)
            dose145.append(res145)
        elif (response.available_capacity_dose1 > 0):
            res118 = create_response_string(date,response)
            dose118.append(res118)
        if(response.available_capacity_dose2 > 0 and response.min_age_limit >= 45):
            res245 = create_response_string(date,response)
            dose245.append(res245)
        elif (response.available_capacity_dose2 > 0):
            res218 = create_response_string(date,response)
            dose218.append(res218)
    
    body145 = sendEmailService.email_body(dose145)
    body118 = sendEmailService.email_body(dose118)
    body245 = sendEmailService.email_body(dose245)
    body218 = sendEmailService.email_body(dose218)
    recipients145 = sendEmailService.get_email_ids(145 )
    recipients118 = sendEmailService.get_email_ids(118)
    recipients245 = sendEmailService.get_email_ids(245)
    recipients218 = sendEmailService.get_email_ids(218)
    sendEmailService.send_multiple_email(recipients145, "Dose 1 Available for 45+", body145)
    sendEmailService.send_multiple_email(recipients118, "Dose 1 Available for 18+", body118)
    sendEmailService.send_multiple_email(recipients245, "Dose 2 Available for 45+", body245)
    sendEmailService.send_multiple_email(recipients218, "Dose 2 Available for 18+", body218)


def create_response_string(date,response):
    response_string = f"Date: {date}\nDistrict:{response.district_name}\nfee type: {response.fee_type}\nmin age limit: {response.min_age_limit}\nname: {response.name}\naddress: {response.address}\nblock name: {response.block_name}\navailable_capacity_dose1: {response.available_capacity_dose1}\navailable_capacity_dose2: {response.available_capacity_dose2}"
    return response_string




