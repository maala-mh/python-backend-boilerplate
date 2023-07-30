from pydantic import BaseModel


class AddFoo(BaseModel):
    email: str
