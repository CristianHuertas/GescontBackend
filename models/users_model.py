from pydantic import BaseModel

class Users(BaseModel):
    username    : str
    password    : str

    class Config:
        orm_mode = True
