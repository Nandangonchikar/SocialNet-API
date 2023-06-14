from typing import Optional
from pydantic import BaseModel, EmailStr
import datetime
#Define a schema for users to send data to post. using pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase): #extend the features of the base class
    pass

class UserCreateResponse(BaseModel):
    id:int
    email:EmailStr
    created_at: datetime.datetime
    class Config:
        orm_mode=True


class PostResponse(PostBase):  #will inherit other 3 fields!!
    id: int
    created_at: datetime.datetime
    owner_id: int
    owner: UserCreateResponse
    class Config:
        orm_mode=True

class UserCreate(BaseModel): 
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id:Optional[str]=None