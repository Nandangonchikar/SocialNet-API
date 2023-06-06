from pydantic import BaseModel

#Define a schema for users to send data to post. using pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int]

class CreatePost(PostBase): #extend the features of the base class
    pass