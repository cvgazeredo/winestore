from pydantic import BaseModel



class CountrySchema(BaseModel):
    id: int
    name: str

