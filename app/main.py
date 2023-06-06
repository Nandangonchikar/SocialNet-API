from typing import Optional
from fastapi import Body, Depends, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session


# local imports
from . import models
from .database import engine,get_db


models.Base.metadata.create_all(bind=engine)

app=FastAPI()


        
#Define a schema for users to send data to post. using pydantic
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int]

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

@app.get("/")
def root():  #Function name doesn't matter
    return {"message": "Welcome to fastAPI learning"} 

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "Success"}
     
#Get all the posts
@app.get("/posts")
def post(): 
    cursor.execute(""" SELECT * FROM posts """)
    my_posts=cursor.fetchall()
    return {"data": my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def createPosts(post: Post):   #return should be 201 for post
    # post_dict=post.dict()
    # post_dict['id']=randint(0,100000)
    # my_posts.append(post_dict)
    cursor.execute(""" INSERT INTO posts(title, content,published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return {"data": new_post}


@app.get("/posts/{id}")  #id id path parameter
def get_post(id: int, response:Response): #Get a single post
    post=find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message": f"No post found with ID: {id}"}
    return {"data": post}   

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    #delete a post
    cursor.execute("""DELETE FROM posts WHERE id =%s RETURNING * """,(str(id)))
    deleted_post=cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post: Post):

    cursor.execute("""UPDATE posts SET title =%s, content =%s , published =%s WHERE id=%s RETURNING *""", (post.title, post.content, post.published,id),)
    updated_post=cursor.fetchone()
    conn.commit()
    print(updated_post)
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    return {"Succesfully updated": updated_post}