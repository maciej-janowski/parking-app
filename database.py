from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

file_location = r'C:\Users\Maciek\PycharmProjects\Python\parking_app\fast_api\parking_api.db'

# creating engine for database
SQLALCHEMY_DATABASE_URL = f"sqlite:///{file_location}?check_same_thread=False"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()