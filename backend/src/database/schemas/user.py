import uuid
from typing import List

from pydantic import BaseModel


class CreateUser(BaseModel):

    name: str
    password: str
    email: str

class ResponseUser(BaseModel):

    id: uuid.UUID
    name: str
    email: str
    is_active: bool

class LoginUser(BaseModel):

    email: str
    password: str

class ListResponseUsers(BaseModel):
    users: List[ResponseUser]
