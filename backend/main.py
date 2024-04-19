from fastapi import FastAPI
from core.config import settings
from db.base_class import Base
from db.session import engine
from apis.base_router import api_router
from fastapi_permissions import configure_permissions
from apis.permissions import ROLES
from starlette.middleware.cors import CORSMiddleware
from fastapi_amis_admin.admin.settings import Settings
from fastapi_amis_admin.admin.site import AdminSite
from fastapi_amis_admin.admin import admin
from db.session import SQLALCHEMY_DATABASE_URL
from db.models.users import User
from db.models.blogs import Blog
from db.admin import register_admin_routes
# function to create table into database 
# def create_tables():
#     Base.metadata.create(bind=engine)

# create app instance
app = FastAPI(
    title= settings.PROJECT_TITLE,
    description="CRUD operations apis",
    terms_of_service="http://www.google.com",
    contact={
        "developer name":"Amol Shewalkar",
        "email":"amol.s@amazatic.com"
    },
    license_info={
        "name":"ABC",
        "url":"http://www.google.com"
    }
)

# Create the AdminSite instance with custom settings
site = AdminSite(settings=Settings(database_url=SQLALCHEMY_DATABASE_URL))

# @site.register_admin
# class UserAdmin(admin.ModelAdmin):
#     page_schema = 'User'
#     # set model
#     model = User
    
# @site.register_admin
# class BlogAdmin(admin.ModelAdmin):
#     page_schema = 'Blog'
#     # set model
#     model = Blog

register_admin_routes(site)

# mount AdminSite instance
site.mount_app(app)
#app.mount('/admin',site)



# create initial database table
@app.on_event("startup")
async def startup():
    await site.db.async_run_sync(Base.metadata.create_all, is_session=False)


# Configure permissions
configure_permissions(app, permission_exception=ROLES.keys)

app.include_router(api_router)

# Setup CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

