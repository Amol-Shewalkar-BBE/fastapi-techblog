from schemas.blogs import CreateBlog, UpdateBlog
from sqlalchemy.orm import Session
from db.models.blogs import Blog
from fastapi import Depends
from db.session import get_db

def create_new_blog(blog:CreateBlog, db:Session, author_id:int = 2):
    blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        auther_id=blog.auther_id
    )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def update_a_blog(id:int, blog:UpdateBlog, db:Session=Depends(get_db), auther_id:int=2):
    obj = db.query(Blog).filter(Blog.id == id)
    if not obj.first():
        pass
    obj.update(blog.dict())
    db.commit()
    return {'blog is updated sucessfully'}

