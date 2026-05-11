from pydantic import BaseModel, Field
from typing import List, Literal
from uuid import uuid4, UUID

class Challenge(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10)
    difficulty: Literal["Easy", "Medium", "Hard"]
    tags: List[str] = []