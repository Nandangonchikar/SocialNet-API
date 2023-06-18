from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# local imports
from . import models
from .database import engine
from .routers import post, user,auth,vote

models.Base.metadata.create_all(bind=engine)


app=FastAPI()

#for allowing cross origin requests, so that we can use this api from other domains
#If we give * api can be accessed from any domain domain ex: www.google.com, www.urwebsite.com
origins=['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

