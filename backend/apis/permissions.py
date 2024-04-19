from fastapi_permissions import Allow, Deny, Authenticated, configure_permissions
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from schemas import users
from core.config import settings
from sqlalchemy.orm import Session
from db.session import get_db
from db.models.users import User

# Define roles and permissions
ROLES = {
    "admin": ["read", "write", "update", "delete"],
    "moderator":["read"],
    "editor": ["read", "update"],
    "author": ["read","write","update", "delete"]
}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token:str = Depends(oauth2_scheme), db:Session =Depends(get_db)):
    credentials_exception =  HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid user credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    try:
        print(type(token))
        print(type(settings.SECRET_KEY))
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHUM)
        print(payload)
        user_id = payload.get("sub")
        role = payload.get("role")
        print(user_id)
        if user_id is None:
            raise credentials_exception
        user = db.query(User).filter(User.id==user_id).first()
        return role

    except JWTError as je:
        print(f"JWTError: {str(je)}")
        raise credentials_exception
    
# define permission service
class PermissionService:
    def has_permission(self, role:str, permission:str):
        return permission in (ROLES.get(role, []))

#Dependancy to check permissions 
# def has_permission(permission:str,permission_service:PermissionService = Depends(),
#                    user:User = Depends(get_current_user)):
#     check_permission = permission_service.has_permission(user.role, permission)
#     if not check_permission:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="permission denied")
#     return check_permission

def has_permission(permission: str):
    async def check_permission(db:Session=Depends(get_db), permissions_service: PermissionService = Depends(),
                               user: User = Depends(get_current_user)):
        #role = db.query(User).filter(User.id==user).first().role
        if not permissions_service.has_permission(user, permission):
            raise HTTPException(status_code=403, detail="Forbidden")
    return check_permission