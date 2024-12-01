import uuid
from typing import Optional

from pydantic import BaseModel


class RequestTransaction(BaseModel):
    amount: float
    category_id: uuid.UUID
    short_description: Optional[str] = None


class CreateTransaction(BaseModel):
    user_id: uuid.UUID
    amount: float
    category_id: uuid.UUID
    short_description: Optional[str] = None
