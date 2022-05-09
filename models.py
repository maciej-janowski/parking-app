from database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column,String,Integer,Float,Boolean,DateTime
# to handle adding url we have to use URLType
from sqlalchemy_utils import URLType
# for indicating the relationship
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(Integer)
    cars = relationship('Car',back_populates='person',lazy='select',cascade = "all,delete",uselist=False)


class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer,primary_key=True)
    plate = Column(String)
    brand = Column(String)
    model = Column(String)
    person_id = Column(Integer,ForeignKey('users.id'),nullable=False)
    person = relationship('User',back_populates='cars')
    parkings = relationship('Parking',back_populates='cars',lazy='select',cascade = "all,delete")


class Parking(Base):
    __tablename__ = 'parkings'
    id = Column(Integer,primary_key=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime,nullable=True)
    cost = Column(Float,nullable=True)
    payment_status = Column(Boolean,nullable=True) 
    car_id = Column(Integer,ForeignKey('cars.id'),nullable=False)
    cars = relationship('Car',back_populates='parkings')

