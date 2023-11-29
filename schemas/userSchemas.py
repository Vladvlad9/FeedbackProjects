from datetime import datetime

from pydantic import BaseModel, Field, field_validator
import re


class UserSchema(BaseModel):
    user_id: int = Field(ge=1)
    phone: str = Field(...)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)

    # @classmethod
    # @field_validator('phone')
    # def check_phone(cls, v):
    #     if not re.match("^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", v):
    #         raise ValueError('Неверный формат российского телефонного номера')
    #     return v


class UserInDBSchema(UserSchema):
    id: int = Field(ge=1)
