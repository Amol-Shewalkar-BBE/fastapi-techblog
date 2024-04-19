from sqlalchemy import (Column, Integer, String, Index, ForeignKey, 
                        Boolean, DateTime, Text, Enum)
from db.base import Base
from sqlalchemy.orm import relationship
#from schemas.users import Roles
from sqlalchemy import Enum

# Define your list of user roles
USER_ROLES = ['admin', 'author', 'moderator', 'editor']
# USER_ROLES = {
#     "admin": "admin",
#     "moderator":"moderator",
#     "editor": "editor",
#     "user": "user"
# }

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    role = Column(Enum(*USER_ROLES, name='user_role_enum'), nullable=False)
    blogs = relationship('Blog', back_populates="author")