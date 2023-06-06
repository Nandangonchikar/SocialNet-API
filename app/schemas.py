from pydantic import BaseModel
import datetime
#Define a schema for users to send data to post. using pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class CreatePost(PostBase): #extend the features of the base class
    pass

class PostResponse(PostBase):  #will inherit other 3 fields!!
    id: int
    created_at: datetime.datetime

    class Config:
        orm_mode=True
