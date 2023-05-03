from pydantic import BaseModel

from schemas import OrderSchema


# class UserSchema(BaseModel):
#     id: int
#     name: str
#     address: str
#     order: OrderSchema

class CreateUserSchema(BaseModel):
    name: str
    address: str
