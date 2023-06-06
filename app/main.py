from typing import Optional
from fastapi import Body, Depends, FastAPI, Response, status, HTTPException
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session


# local imports
from . import models
from .database import engine,get_db
from . import schemas

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

@app.get("/")
def root():  #Function name doesn't matter
    return {"message": "Welcome to fastAPI learning"} 
     
#Get all the posts
@app.get("/posts")
def post(db: Session = Depends(get_db)): 
    # cursor.execute(""" SELECT * FROM posts """)
    # my_posts=cursor.fetchall()
    my_posts=db.query(models.Post).all()    #through sql alchemy
    return {"data": my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def createPosts(post: schemas.CreatePost,db: Session = Depends(get_db)):   #return should be 201 for post
    # post_dict=post.dict()
    # post_dict['id']=randint(0,100000)
    # my_posts.append(post_dict)
    # cursor.execute(""" INSERT INTO posts(title, content,published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    # new_post=models.Post(title=post.title, content=post.content, published=post.published) can use unpacking instead of these

    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  #return the new data created in the new_post variable
    return {"data": new_post}


@app.get("/posts/{id}")  #id id path parameter
def get_post(id: int, response:Response,db: Session = Depends(get_db)): #Get a single post
    # post=find_post(id)

    my_post=db.query(models.Post).filter(models.Post.id == id).first()
  
    if not my_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message": f"No post found with ID: {id}"}
    return {"data": my_post}   

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db)):
    #delete a post through pyscop
    # cursor.execute("""DELETE FROM posts WHERE id =%s RETURNING * """,(str(id)))
    # deleted_post=cursor.fetchone()
    # conn.commit()

    # Using SQLalchemy ORM
    deleted_post=db.query(models.Post).filter(models.Post.id == id)
    if deleted_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    deleted_post.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int, post: schemas.CreatePost,db: Session = Depends(get_db)):
    # USING pyscop
    # cursor.execute("""UPDATE posts SET title =%s, content =%s , published =%s WHERE id=%s RETURNING *""", (post.title, post.content, post.published,id),)
    # updated_post=cursor.fetchone()
    # conn.commit()
  
    #using SQLalchemy
    updated_post=db.query(models.Post).filter(models.Post.id == id)
    if updated_post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
    updated_post.update(post.dict(),synchronize_session=False)
    db.commit()
    return {"Succesfully updated": updated_post.first()}