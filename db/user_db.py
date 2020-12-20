from typing import Dict
from pydantic import BaseModel
from pprint import pprint
from fastapi import HTTPException
from models.user_models import UserUpdated

class UserInDB(BaseModel): #así se hace la herencia le python
    # Aca se dejan los demas en False para que el usuario pueda
    # crease solo con usuario y contraseña
    username: str
    password: str
    nombre: str = False
    apellido: str = False
    correo: str = False
    celular: int = False
    rol: str = False

database_users = Dict[str, UserInDB]

database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "nombre":"Camilo",
                            "apellido":"Perez",
                            "correo":"camper@gmail.com",
                            "celular":3146785643,
                            "rol":"admin"}),
    "esteban15": UserInDB(**{"username":"esteban15",
                            "password":"root1",
                            "nombre":"Esteban",
                            "apellido":"Perez",
                            "correo":"esteper@gmail.com",
                            "celular":3146975643,
                            "rol":"guest"}),
    "Jaime12": UserInDB(**{"username":"Jaime12",
                           "password":"Jaime123",
                           "nombre":"Jaime",
                           "apellido":"Hernandez",
                           "correo":"jaime123@hotmail.com",
                           "celular":3102582585,
                           "rol":"admin"}),
    "Julio987":UserInDB(**{"username":"Julio987",
                           "password":"Julio987",
                           "nombre":"Julio",
                           "apellido":"Comesaña",
                           "correo":"julio.comesana@gmail.com",
                           "celular":3109876543,
                           "rol":"user"}),
    "Hernan.Perez":UserInDB(**{"username":"Hernan.Perez", 
                               "password":"Pereceras",
                               "nombre":"Hernan",
                               "apellido":"Perez",
                               "correo":"hernan.perez@hotmail.com",
                               "celular":3009877845,
                               "rol":"guest"}),
    "FreeLunch":UserInDB(**{"username":"FreeLunch",
                            "password":"987654321",
                            "nombre":"Duvan",
                            "apellido":"Camelo",
                            "correo":"Duvan@yahoo.es",
                            "celular":3153698754,
                            "rol":"user"}),
}

def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_password(name:str, oldpass: str, newpass:str, confnewpass:str):
    user_in_db = get_user(name)
    if user_in_db == None:
        return None
    elif oldpass != user_in_db.password:
        raise HTTPException(status_code=409,detail="Contraseña no valida")
    elif user_in_db.password == oldpass:
        if newpass != confnewpass:
            raise HTTPException(status_code=409,detail="Contraseñas no coinciden")
        user_in_db.password = newpass
        return UserUpdated (username=name, apellido=user_in_db.apellido, correo=user_in_db.correo)


def create_user(new_user: UserInDB):
    if new_user.username in database_users.keys():
        return None
    else:
        database_users[new_user.username]= new_user
        return database_users[new_user.username]

def login(name: str, contra: str):
    for i,j in database_users.items():
        if name == i and contra == j.password:
            print("Match")