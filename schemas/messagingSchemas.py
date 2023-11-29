from datetime import datetime
from pydantic import BaseModel, Field


class MessagingSchemas(BaseModel):
    user_id: int = Field(ge=1)
    message: str
    is_processed: bool


class MessagingInDBSchema(MessagingSchemas):
    id: int = Field(ge=1)
