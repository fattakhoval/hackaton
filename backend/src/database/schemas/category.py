from pydantic import BaseModel

from src.database.models import TransactionType


class NewCategory(BaseModel):
    name: str
    type: TransactionType
