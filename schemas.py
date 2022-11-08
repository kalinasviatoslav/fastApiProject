from pydantic import BaseModel, Field


class CarBase(BaseModel):
    manufacturer_id: int
    model_id: int


class CarCreate(CarBase):
    vin_code: str = Field(..., min_length=17, max_length=17, example='SCA1S684X4UX07444')


class Car(CarBase):
    id: int

    class Config:
        orm_mode = True

