from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String(50), nullable=False)
    location = Column(String, nullable=False)
    address = Column(String(500), nullable=False)
    postcode = Column(Integer, nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    note = Column(String(50), nullable=False)
    is_primary = Column(Boolean, nullable=False)