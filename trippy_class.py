from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    user_id: int
    username: str
    password: str

    def check_password(self, input_password: str) -> bool:
        return self.password == input_password
    
class Order(BaseModel):
    order_id: int
    user_id: int
    package_id: int
    service_id:int

class Service(BaseModel):
    service_id: int
    service_price: float
    air_id: Optional[int] = None
    train_id: Optional[int] = None
    guide_id: Optional[int] = None
    lunch_id: Optional[int] = None
    hotel_id: Optional[int] = None


class Air(BaseModel):
    air_id: int
    air_code: str
    air_price: float
    air_start_place: str
    air_end_place:str
    
class Train(BaseModel):
    train_id: int
    train_code: str
    train_price: float
    train_start_place: str
    train_end_place: str
    
class Guide(BaseModel):
    guide_id: int
    guide_place: str
    guide_price: float
    
class Lunch(BaseModel):
    lunch_id: int
    lunch_price: float
    lunch_place: str
    service_provider_id: int
    
class Hotel(BaseModel):
    hotel_id: int
    hotel_price_sum: float
    hotel_place_sin: float
    hotel_place: str
    hotel_time: int
    service_provider_id: int
    
class Service_provider(BaseModel):
    service_provider_id: int
    provider_name: str
    provider_place: str
    provider_tel: str
    provider_eml: str

class Package(BaseModel):
    package_id: int
    package_price: float
    place: str
    time: int
    air_id: Optional[int] = None
    train_id: Optional[int] = None
    guide_id: Optional[int] = None
    lunch_id: Optional[int] = None
    hotel_id: Optional[int] = None
