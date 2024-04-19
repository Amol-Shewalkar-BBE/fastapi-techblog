from fastapi import APIRouter
from apis.v1 import router_user, router_blog, router_login


api_router = APIRouter()

api_router.include_router(router_user.router, prefix='/users',tags=['users'])
api_router.include_router(router_blog.router, prefix='/blogs',tags=['blogs'])
api_router.include_router(router_login.router, prefix='/login', tags=['login'])