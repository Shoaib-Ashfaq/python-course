from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,  sessionmaker

# Database connection string
DATABASE_URL = "sqlite:///./database.db"

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()
def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
