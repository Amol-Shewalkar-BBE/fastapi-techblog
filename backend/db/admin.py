from fastapi_amis_admin.admin import admin
from db.models.users import User
from db.models.blogs import Blog
from db.session import SQLALCHEMY_DATABASE_URL
from db.base import Base

# # Create the AdminSite instance with custom settings
# site = AdminSite(
#     settings=Settings(
#         database_url_async= SQLALCHEMY_DATABASE_URL
#     )
# )

# Define function to register admin routes
def register_admin_routes(site):
    @site.register_admin
    class UserAdmin(admin.ModelAdmin):
        page_schema = 'User'
        model = User
        
    @site.register_admin
    class BlogAdmin(admin.ModelAdmin):
        page_schema = 'Blog'
        model = Blog

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



