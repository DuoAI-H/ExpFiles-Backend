from pydantic import BaseModel

class UserOut(BaseModel):
    username: str
    nombre: str
    apellido: str = False
    correo: str = False
    celular: int = False
    rol: str = False

class passUpdate(BaseModel):
    username: str
    old_password: str
    new_password: str
    conf_new_pass: str

class passOut(BaseModel):
    password: str

class UserUpdated(BaseModel):
    username: str
    apellido: str = False
    correo: str = False
    estado:str = "Actualizado"