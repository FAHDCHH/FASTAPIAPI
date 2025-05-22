from pydantic import BaseModel, EmailStr
import uuid
class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: uuid.UUID
    firstname: str
    lastname: str
    email: EmailStr

    class Config:
        orm_mode = True

class LoginSchema(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
