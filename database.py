import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://data_qqmk_user:mToW3AQnlj1cCoUWeHvmKbGyl21qoXBU@dpg-cq607hl6l47c738scgag-a.oregon-postgres.render.com/data_qqmk"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
