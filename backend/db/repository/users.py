from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.models import users
from core.hashing import Hasher


def Create_new_user(user:UserCreate, db:Session):
    user = users.User(
        first_name = user.first_name,
        last_name = user.last_name,
        email = user.email,
        username = user.username,
        password = Hasher.get_password_hash(user.password),
        is_active = True,
        role = user.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user