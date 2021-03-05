from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import cgi

api = FastAPI()

#origin = ['*']
#api.add_middleware(CORSMiddleware,allow_origins = origin,allow_credentials = True,allow_methods = ['*'],allow_headers = ['*'])

class info(BaseModel):
    name: str
    veh_name: str
    prcs_date: str
    ph_no: str

@api.get("/data")
def veh_data():
    return "Vehicle Information"

@api.post("/post")
def create(name_var: info):
    name_encoded = jsonable_encoder(name_var)
    print(name_encoded)
    name = name_encoded["name"]
    print("Name: ",name)
    veh_name = name_encoded["veh_name"]
    print("Vehicle name: ",veh_name)
    prcs_date = name_encoded["prcs_date"]
    print("Purchase date: ",prcs_date)
    ph_no = name_encoded["ph_no"]
    print("Phone number: ",ph_no)
    return name,veh_name,prcs_date,ph_no

form = cgi.FieldStorage()
d = form.getvalue('veh_data')