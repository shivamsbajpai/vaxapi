from app.common.getUserDetails import get_user_details
from app.common.findVaccineSlot import find_vaccine_slot
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_utils.tasks import repeat_every
from .data.database import engine, Base
from .routers import userDetailsRouter
from app.data import database
import app.common.config as config

Base.metadata.create_all(engine)

tags_metadata = [
    {
        "name": "Vax API",
        "externalDocs": {
            "description": "Created with love ❤️. Developer wants to connect with you",
            "url": "https://tinyurl.com/3jyarv3h",
        },
    },
]

app = FastAPI(title="Find your slot", openapi_tags=tags_metadata)
version_prefix = '/api/v1'

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

config.user_details = get_user_details()

@app.on_event("startup")
@repeat_every(seconds= 60*60)
def function_to_call_every_hour():
    config.user_details = get_user_details()


@app.on_event("startup")
@repeat_every(seconds= 60)
def function_to_call_every_minute():
    find_vaccine_slot()



app.include_router(userDetailsRouter.router,prefix=version_prefix)
