from fastapi import Path
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/v1/vehicle/get/{vin_code}')
async def get_car_by_vin_code(vin_code: str = Path(..., min_length=17, max_length=17),
                              db: Session = Depends(get_db)) -> schemas.Car:
    car = crud.get_car_by_vin_code(vin_code, db)
    return schemas.Car(id=car.id, manufacturer_id=car.manufacturer_id, model_id=car.model_id)


@app.post('/v1/vehicle/')
async def create_car(car: schemas.CarCreate, db: Session = Depends(get_db)) -> schemas.Car:
    return crud.add_car(car, db)
