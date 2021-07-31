import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:root@localhost:5432/vaccineDetails"


if(os.environ.get("ENVIRONMENT") == "STAGING"):
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri=uri.replace("postgres://","postgresql://",1)
    SQLALCHEMY_DATABASE_URL = uri

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
