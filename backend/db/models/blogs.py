from sqlalchemy import (Column, Integer, String, Index, ForeignKey, Boolean, DateTime, Text)
from db.base import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    id =  Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    auther_id = Column(Integer, ForeignKey('user.id'))
    author = relationship('User', back_populates="blogs")
    is_active = Column(Boolean, default=False)