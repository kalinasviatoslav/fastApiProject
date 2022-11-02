from sqlalchemy import Column, Integer, String, MetaData
from database import Base
from database import engine


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    manufacturer_id = Column(Integer)
    model_id = Column(Integer)
    vin_code = Column(String)


meta = MetaData()
meta.create_all(engine)
