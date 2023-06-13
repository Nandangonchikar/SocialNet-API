from fastapi import  Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas,oauth2
from ..database import get_db

router=APIRouter(
        prefix="/posts",
        tags=['posts']
        )

# @router.get("/")
# def root():  #Function name doesn't matter
#     return {"message": "Welcome to fastAPI learning"} 
     
#Get all the posts
@router.get("/",response_model=List[schemas.PostResponse])
def post(db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)): 
    # cursor.execute(""" SELECT * FROM posts """)
    # my_posts=cursor.fetchall()
    my_posts=db.query(models.Post).all()    #through sql alchemy
    return my_posts

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def createPosts(post: schemas.CreatePost,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):   #return should be 201 for post
    # post_dict=post.dict()
    # post_dict['id']=randint(0,100000)
    # my_posts.routerend(post_dict)
    # cursor.execute(""" INSERT INTO posts(title, content,published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()
    # new_post=models.Post(title=post.title, content=post.content, published=post.published) can use unpacking instead of these
    print(user_id)
    new_post=models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  #return the new data created in the new_post variable
    return new_post


@router.get("/{id}",response_model=schemas.PostResponse)  #id id path parameter
def get_post(id: int, response:Response,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)): #Get a single post
    # post=find_post(id)

    my_post=db.query(models.Post).filter(models.Post.id == id).first()
  
    if not my_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message": f"No post found with ID: {id}"}
    return  my_post   

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
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

@router.put("/{id}")
def update_post(id:int, post: schemas.CreatePost,db: Session = Depends(get_db),response_model=schemas.PostResponse,user_id:int=Depends(oauth2.get_current_user)):
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