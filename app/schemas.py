from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint

# region USER REQUEST: User sending data to server


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserRequest(UserBase):
    pass

# endregion

# region USER RESPONSE: Server sending data to user


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

# endregion

# region USER LOGIN


class UserLogin(UserBase):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None

# endregion

# region POST REQUEST: sending data to server


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostRequest(PostBase):
    pass

# endregion

# region POST RESPONSE: Server sending data to user


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner: UserResponse

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

# endregion

# region VOTE REQUEST/RESPONSE

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

# endregion