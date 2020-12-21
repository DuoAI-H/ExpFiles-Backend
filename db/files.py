from typing import Dict
from pydantic import BaseModel
import json

with open('db/files.json',encoding='utf-8') as f: 
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

#Devuelve una lista con las llaves que contienen alguna concidencia
def found_by (keyword_s: str):
    list_related = list()
    # Items son las llaves
    for items in database_files.keys():
        # item es la caracteristica objeto
        for item in database_files[items]:
            if item[0] not in ["file_id","user_auth"]:
                search = item[1].strip().lower()
                keyw = keyword_s.strip().lower()
                if (keyw in search) and (items not in list_related):
                    list_related.append(items)
    return list_related

def request(user_key: list):
    
    return None

def get_equal(keyword_s:str):
    list_related=found_by(keyword_s)
    list_auth=request(list_related)
    return list_auth

#get_equal("2019")
found_by("Type")