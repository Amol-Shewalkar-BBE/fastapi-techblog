from fastapi import FastAPI
from core.config import settings

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