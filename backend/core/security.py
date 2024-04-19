from datetime import datetime, timedelta
from jose import jwt
from core.config import settings
from schemas.users import TokenData


def create_jwt_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHUM)
    return encode_jwt