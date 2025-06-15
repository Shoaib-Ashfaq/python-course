from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import modals, schemas
from database import SessionLocal, engine, Base
from typing import List

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    """Dependency to get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.User, db: Session = Depends(get_db)):

    """Check if the user already exists and create a new user if not."""
    db_user = db.query(modals.User).filter(modals.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    """Create a new user."""
    db_user = modals.User(name=user.name, email=user.email, age=user.age, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/login/", response_model=schemas.User)
def login_user(login_req: schemas.LoginReq, db: Session = Depends(get_db)):
    """Authenticate a user by email and password."""
    db_user = db.query(modals.User).filter(modals.User.email == login_req.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    # Here you would typically verify the hashed password
    # For simplicity, we assume the password is correct
    return db_user


@app.get("/users/", response_model=List[schemas.User])
def read_all_users(db: Session = Depends(get_db)):
    """Fetch all users from the database."""
    users = db.query(modals.User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
