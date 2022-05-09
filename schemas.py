
from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime
# from datetime import date

    


class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    phone:int
    class Config():
        orm_mode=True


class Car(BaseModel):
    plate:str
    brand:str
    model:str
    person_id:int
    
    class Config():
        orm_mode=True

# class used when parking is started. Cost is set to zero and payment is set as "not paid"
class Parking(BaseModel):
    start_time:datetime
    cost:Optional[float] = 0
    payment_status:Optional[bool] = False
    car_id:int

    class Config():
        orm_mode=True


class UserFirstLastName(BaseModel):
    first_name:str
    last_name:str
    class Config():
        orm_mode=True

# class for updating parking data once parking is initiated
class UpdateParking(BaseModel):
    end_time:datetime
    cost:float
    class Config():
        orm_mode=True


