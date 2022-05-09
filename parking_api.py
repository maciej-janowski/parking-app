from fastapi import FastAPI,Depends
# from typing import Optional
from schemas import User,Parking,Car
import models
from database import engine
from database import get_db
from sqlalchemy.orm import Session
import schemas
# import os
import pandas as pd
import datetime




models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 1 Create user


@app.post('/create_user')
def creat_iuser(*,db:Session = Depends(get_db),user:User):
    # passing dictionary to model so that fields are populated
    new_user = models.User(**user.dict())
    # adding to session
    db.add(new_user)
    # moving to database from session
    db.commit()
    db.refresh(new_user)
    # returning created user
    return new_user



# 2 get user
@app.get('/user/{id}',response_model=schemas.UserFirstLastName)
def get_user(id:int,db:Session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    return user


# 3 get all users
@app.get('/all_users')
def get_all_users(db:Session= Depends(get_db)):
    all_users = db.query(models.User).all()
    return all_users


# 4 create car
@app.post('/create_car')
def create_car(*,db:Session = Depends(get_db),car:Car):
    # passing dictionary to model so that fields are populated
    new_car = models.Car(**car.dict())
    # adding to session
    db.add(new_car)
    # moving to database from session
    db.commit()
    db.refresh(new_car)
    # returning created car
    return new_car

# 5 get car
@app.get('/car/{id}')
def get_car(id:int,db:Session= Depends(get_db)):
    car = db.query(models.Car).filter(models.Car.id==id).first()
    return car

# 6 get all cars
@app.get('/all_cars')
def get_all_cars(db:Session= Depends(get_db)):
    all_cars = db.query(models.Car).all()
    return all_cars

# 7 create parking
@app.post('/create_parking')
def create_parking(*,db:Session = Depends(get_db),parking:Parking):
    # passing dictionary to model so that fields are populated
    new_parking = models.Parking(**parking.dict())
    # adding to session
    db.add(new_parking)
    # moving to database from session
    db.commit()
    db.refresh(new_parking)
    # returning created parking
    return new_parking
    
# 7 # 8 stop parking
@app.post('/stop_parking')
def stop_parking(*,db:Session = Depends(get_db),parking_id:int):
    # finding parking for update
    parking_update = db.query(models.Parking).get(parking_id)
    # creating timestamp from start time column
    start_time = pd.to_datetime(parking_update.start_time)
    # calculating time when parking is finished
    end_time = datetime.datetime.now() - datetime.timedelta(hours=2)
    # calculating total seconds for parking
    parking_time = end_time - start_time
    # calculating cost
    cost = (int(parking_time.seconds/60) * 7)/100
    # assigning new values to database object
    parking_update.end_time = end_time
    parking_update.cost = cost
    db.commit()
    # returning message
    return f"Parking {parking_id} has been updated"


# 9 get parking
@app.get('/parking/{id}')
def get_parking(id:int,db:Session= Depends(get_db)):
    parking = db.query(models.Parking).filter(models.Parking.id==id).first()
    return parking

# 10 get all parkings
@app.get('/all_parkings')
def get_all_parkings(db:Session= Depends(get_db)):
    all_parkings = db.query(models.Parking).all()
    return all_parkings




