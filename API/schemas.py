from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., description="The name of the user")
    email: EmailStr = Field(..., description="The email address of the user")
    age: int = Field(..., ge=0, description="The age of the user, must be a non-negative integer")
    hashed_password: str = Field(..., description="The hashed password of the user")


class LoginReq(BaseModel):
    email: EmailStr = Field(..., description="The email address of the user")
    password: str = Field(..., description="The password of the user")
