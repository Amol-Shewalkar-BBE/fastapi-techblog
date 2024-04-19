from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.users import UserCreate, ShowUser
from db.repository.users import Create_new_user 


router = APIRouter()

@router.post('/', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(user:UserCreate, db:Session = Depends(get_db)):
    user = Create_new_user(user, db)
    return user