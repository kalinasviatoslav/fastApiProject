from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException


def add_car(car: schemas.CarCreate, db: Session) -> schemas.Car | str:
    if get_car_by_vin_code(car.vin_code, db) is None:
        new_car = models.Car(manufacturer_id=car.manufacturer_id,
                             model_id=car.model_id, vin_code=car.vin_code)
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return new_car
    else:
        raise HTTPException(status_code=404, detail='file with this vincode already exist in db')


def get_car_by_vin_code(vin_code: str, db: Session, ) -> schemas.Car | None:
    return db.query(models.Car).filter(models.Car.vin_code == vin_code).first()
