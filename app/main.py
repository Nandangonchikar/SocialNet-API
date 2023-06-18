from fastapi import FastAPI

# local imports
from . import models
from .database import engine
from .routers import post, user,auth,vote

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():  #Function name doesn't matter
    return {"message": "Welcome to fastAPI learning"} 


# my_posts=[{"title" :"title of the post", "content" :"content of the post", "id":1},
#           {"title" :"title of the second post", "content" :"content of the second post", "id":2}]

# def find_post(id):
#     # for p in my_posts:
#     #     if p["id"]==id:
#     #         return p
#     #Code updated to work with postgres data base
#     cursor.execute(""" SELECT * FROM posts WHERE id=%s """,(str(id)))
#     found_post=cursor.fetchone()
#     return found_post   
 
# def find_index_post(id):
#     for index,p in enumerate(my_posts):
#         if p["id"]==id:
#             return index

