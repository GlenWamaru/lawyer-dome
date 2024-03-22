from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the database connection URL
DATABASE_URL = "sqlite:///../../lawyers_dome.db"

# Create a database engine
engine = create_engine(DATABASE_URL)

# Create a sessionmaker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a function to get a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
