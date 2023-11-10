from enum import Enum
from pydantic import BaseModel, Field


class DogType(Enum):
    terrier = "terrier"
    bulldog = "bulldog"
    dalmatian = "dalmatian"


class Timestamp(BaseModel):
    id: int
    timestamp: int


class Dog(BaseModel):
    name: str
    pk: int = Field(default=None)  # добавляем Field(default=None), т.к. в OpenAPI-описании это свойство необязательное
    kind: DogType
