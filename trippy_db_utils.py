# author : XiaoyuYuan
# des: for connect to db
import sqlite3
from trippy_class import *
from typing import List, Tuple, Generic, TypeVar

DB_PATH = 'Trippy-v2.db'  # database name
DataT = TypeVar("DataT")  # define type var -> DataT
# conn = sqlite3.connect(DB_PATH)

def tuple2dataclass(tuple: Tuple, dataT: Generic[DataT]) -> DataT:
    '''Convert tuple to a dataclass'''
    if tuple is None:
        return
    attibutes = dataT.__fields__.keys()
    d = {}
    for i, a in enumerate(attibutes):
        if i < len(tuple):
            d.update({a: tuple[i]})
    d = dataT.parse_obj(d)
    print(d)
    return d

def add_user_information(username: str, password: str) -> User:
    with sqlite3.connect(DB_PATH) as c:
        cur = c.cursor()
        cur.execute("""
                    insert into user (username, password) 
                    values (:username, :password)
                """, {"username": username, "password": password})
        c.commit()
        return get_user_by_username(username)

def get_user_by_username(username: str) -> User:
    with sqlite3.connect(DB_PATH) as c:
        cur = c.cursor()
        cur.execute("""
            SELECT * FROM user WHERE username=:username
        """, {"username": username})
        res = cur.fetchone()
        user = tuple2dataclass(res, User)
        return user

def check_user_information(username: str, input_password: str) -> bool:
    user_information = get_user_by_username(username)
    if user_information is None:
        return
    return user_information.check_password(input_password)

#get_user_by_username('test')
#print(check_user_information('test','000305xyy'))