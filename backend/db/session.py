from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator

# Database url
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Start the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SESSIONLOCAL = sessionmaker(bind=engine,autoflush=False,autocommit=False)

# starting session
def get_db() ->  Generator:
    db=SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()