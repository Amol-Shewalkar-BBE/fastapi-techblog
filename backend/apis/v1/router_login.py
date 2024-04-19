from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from core.hashing import Hasher
from db.session import get_db
from db.models.users import User
from core.security import create_jwt_token

router = APIRouter()

def authenticate_user(email:str, password:str, db:Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='Invalid user')
    
    if not Hasher.verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail='password is invalid')
    return user

@router.post('/')
def Login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user = authenticate_user(request.username,request.password,db)
    print(user)
    print(user.id)
    if not user:
        raise HTTPException(
                            status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid user credentials",
                            headers={"WWW-Authenticate":"Bearer"}
                        )
    access_token = create_jwt_token(data={'sub':str(user.id),'role':user.role})
    return {"access_token":access_token, "token_type":"bearer"}
