from typing import List, Optional

from pydantic import BaseModel


class address(BaseModel):
    nickname: str
    location: str
    address: str
    postcode: int
    city: str
    state: str
    note: str
    is_primary: bool

    class Config:
        orm_mode = True
