from typing import List

from pydantic import BaseModel

from model import Country


class CountrySchema(BaseModel):
    id: int
    name: str

