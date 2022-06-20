from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from schema.user_schema import DataUser
from typing import List, Union

user = APIRouter()

@user.get("/")
def root():
    return "Hello Palenca"

@user.post("/uber/login")
def user_login(data_user: DataUser):
    if data_user.password == "MyPwdChingon123" and data_user.email == "pierre@palenca.com":
        return {
            "message": "SUCCESS",
            "access_token": "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5"
        }

    response = {
        "message": "CREDENTIALS_INVALID",
        "details": "Incorrect username or password"
    }
    return JSONResponse(status_code=401, content=response)

@user.get("/uber/profile/{access_token}")
def get_user(access_token):
    if access_token == "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5":
        return {
            "message": "SUCCESS",
            "platform": "uber",
            "profile": {
                    "country": "mx",
                    "city_name": "Ciudad de Mexico",
                    "worker_id": "34dc0c89b16fd170eba320ab186d08ed",
                    "first_name": "Pierre",
                    "last_name": "Delarroqua",
                    "email": "pierre@palenca.com",
                    "phone_prefix": "+52",
                    "phone_number": "5576955981",
                    "rating": "4.8",
                    "lifetime_trips": 1254
                }
        }
    
    response = {
        "message": "CREDENTIALS_INVALID",
        "details": "Incorrect username or password"
    }
    return JSONResponse(status_code=401, content=response)
