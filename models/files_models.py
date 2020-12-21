from pydantic import BaseModel

class FileOut(BaseModel):
    file_name: str
    data_upload: str
    date_expired: str
    file_uploaded: str

class HintSearch(BaseModel):
    keyword_s: str
    user_auth: str