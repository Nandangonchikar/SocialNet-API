from fastapi import  Depends, FastAPI, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session

from .. import schemas, database, models, oauth2
from ..database import get_db

router=APIRouter(
    prefix="/vote",
    tags=['vote']
    )

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):

    #if user tries to vote on an post which is not there.
    post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id {vote.post_id} not found")

    vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id, models.User.id==current_user.id)
    found_vote=vote_query.first()
    if(vote.dir == 1): #upvote
        if(found_vote):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user {current_user.id} has already voted for this post")
        new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"Successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message":"Successfully deleted vote"}
