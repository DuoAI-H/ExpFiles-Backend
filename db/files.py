from typing import Dict
from pydantic import BaseModel
import json

with open('db/files.json',encoding='utf-8') as f : 
    data = json.load(f)


class FilesDB(BaseModel): 
    file_id: str
    file_name: str
    user_auth: str 
    data_upload: str 
    date_expired: str 
    file_uploaded: str 

database_files = Dict[str, FilesDB]
datasample = dict()

for item in data:
    idd = item["file_id"]
    datasample[idd] = FilesDB(**item)

database_files = datasample

# Retorna el item del json
def get_item(file_id: str):
    if file_id in database_files.keys():
        return database_files[file_id].dict()
    else:
        return None

#Devuelve una lista con las llaves que contienen alguna concidencia
def found_by (keyword_s: str):
    list_related = list()
    for items in database_files.keys():
        for item in database_files[items]:
            if item[0] not in ["file_id","user_auth"]:
                search = item[1].strip().lower()
                keyw = keyword_s.strip().lower()
                if (keyw in search) and (items not in list_related):
                    list_related.append(items)
    return list_related

def request(user_key: list, auth: str):
    list_auth = list()
    for id_file in user_key:
        handler = get_item(id_file)
        if auth in handler["user_auth"]:
            list_auth.append(id_file)
    return list_auth

def get_equal(keyword_s:str, user_auth: str):
    list_related=found_by(keyword_s)
    list_auth=request(list_related, user_auth)
    return list_auth