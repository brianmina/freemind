from typing import List, Optional

from sqlalchemy_utils import EmailType

from .models import Role
from datetime import date

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    roles: List[Role]
    dob: Optional[date] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

    """
    roles : List(Role)
    first_name = Column(Unicode(50))
    last_name = Column(Unicode(50))
    email = Column(EmailType)
    password = Column(PasswordType(schemes=[
        'pbkdf2_sha512',
        'md5_crypt'
    ]))
    # password = Column(PasswordType)
    dob = Column(Date)
    is_active = Column(Boolean, default=True)
    """