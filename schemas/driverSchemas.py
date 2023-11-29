from pydantic import BaseModel, Field


class DriverSchema(BaseModel):
    driverName: str
    cardNumber: int
    driver_profile_id: str
    dayNorm: int
    is_transaction: bool


class DriverInDBSchema(DriverSchema):
    id: int = Field(ge=1)
