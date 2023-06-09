from typing import List, Optional
from fastapi import FastAPI, Response, status, HTTPException
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
# local imports
from . import models,schemas,utils
from .database import engine,get_db
from .routers import post, user,auth

models.Base.metadata.create_all(bind=engine)

app=FastAPI()


while True:
        try:
            conn=psycopg2.connect(host='localhost',database='fastAPi',
                                 user='postgres',password='admin',
                                 cursor_factory=RealDictCursor)
            cursor=conn.cursor()
            print("DB connection Successfull!!")
            break 
        except Exception as e:
            print("Could not connect to db")
            print(e)
            time.sleep(3)

my_posts=[{"title" :"title of the post", "content" :"content of the post", "id":1},
          {"title" :"title of the second post", "content" :"content of the second post", "id":2}]

def find_post(id):
    # for p in my_posts:
    #     if p["id"]==id:
    #         return p
    #Code updated to work with postgres data base
    cursor.execute(""" SELECT * FROM posts WHERE id=%s """,(str(id)))
    found_post=cursor.fetchone()
    return found_post   
 
def find_index_post(id):
    for index,p in enumerate(my_posts):
        if p["id"]==id:
            return index

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
