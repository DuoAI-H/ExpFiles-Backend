from db.user_db import UserInDB, get_user, update_password, create_user, login
from models.user_models import UserOut, passOut, passUpdate
from db.files import FilesDB, get_data

import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

###############################################
"""
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8000",
    "https://expfiless.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""
###############################################

@api.get("/user/leerUsuario/{username}")
async def get_data(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.put("/user/updateUser/")
async def update_pass(name: passUpdate):
    user_in_db = get_user(name.username)
    print(name.username)
    if user_in_db == None:
        raise HTTPException(status_code=404,detail="El usuario no existe")
    else:
        actualizacion = update_password(name.username,name.old_password,name.new_password, name.conf_new_pass)
        return actualizacion

@api.post("/user/createUser/")
async def new_user(newuser: UserInDB):
    #409 o 403 como errores HTTP
    response_new_user = create_user(newuser)
    if response_new_user == None:
        raise HTTPException(status_code=409, detail= "Conflicto, el usuario ya existe")
    else:
        return response_new_user

@api.get("/user/Buscar/{keyword_s}")
async def get_data(keyword_s: str):
    #Aca busco todo lo que concuerde, con la funcion get
    id_items_related = get_equal(keyword_s)