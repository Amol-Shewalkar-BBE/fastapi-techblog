from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import Enum
from typing import Optional

# class Roles(str, Enum):
#     admin = 'admin',
#     auther = 'auther'
#     editor = 'editor'


class UserCreate(BaseModel):
    first_name : str
    last_name : str
    email : EmailStr
    username : str =  Field(..., min_length=4)
    password : str = Field(..., min_length=4)
    is_active : bool
    role : str

class ShowUser(BaseModel):
    username : str 
    email : EmailStr
    is_active : bool 
    role : str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    user_id:Optional[int]=None
    username:Optional[str]=None
    email:Optional[EmailStr]=None
    role:Optional[str]=None