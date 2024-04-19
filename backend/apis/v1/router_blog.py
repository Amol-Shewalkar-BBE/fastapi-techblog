from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from schemas.blogs import ShowBlog, CreateBlog, UpdateBlog
from db.session import get_db
from db.repository.blogs import create_new_blog, update_a_blog
from db.models import blogs
from typing import List
from apis.permissions import has_permission, get_current_user
from db.models.users import User

router = APIRouter()

@router.post('/', response_model=ShowBlog, status_code=status.HTTP_201_CREATED,dependencies=[Depends(has_permission("write"))])
def create_blog(blog:CreateBlog, db:Session=Depends(get_db),user: User = Depends(get_current_user)):
    blog = create_new_blog(blog=blog, db=db, author_id=2)
    return blog

# route for retriving all blogs
@router.get('/', response_model=list[ShowBlog], status_code=status.HTTP_200_OK,
            dependencies=[Depends(has_permission("read"))])
def get_all_blogs(db:Session=Depends(get_db),user: User = Depends(get_current_user)):
    objects = db.query(blogs.Blog).all()
    return objects

# retriving single blog object
@router.get('/{id}', response_model=ShowBlog,status_code=status.HTTP_200_OK,
            dependencies=[Depends(has_permission("read"))])
def get_blog(id:int, db:Session= Depends(get_db),user: User = Depends(get_current_user)):
    blog = db.query(blogs.Blog).filter(blogs.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="blog not found")
    
    return blog

# updating blog
@router.put('/{id}',status_code=status.HTTP_205_RESET_CONTENT,
            dependencies=[Depends(has_permission("update"))])
def update_blog(id:int, blog:UpdateBlog, db:Session = Depends(get_db),user: User = Depends(get_current_user)):
    blog = update_a_blog(id=id, blog=blog, db=db, auther_id=2)
    if not blog:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="blog not found")

    return blog

# deleting single object from table
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(has_permission("delete"))])
def delete_blog(id:int, db:Session = Depends(get_db),user: User = Depends(get_current_user)):
    db.query(blogs.Blog).filter(blogs.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {"Single object is delete with id = {id}"}