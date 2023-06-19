from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool
    password: str

users_db = {
    "mouredev":{
        "username":"mouredev",
        "fullname":"Brais Moure",
        "email":"mouredev@gmail.com",
        "disabled":False,
        "password":"123456"
    },
    "ferran":{
        "username":"ferranmar00",
        "fullname":"Ferran Marquez",
        "email":"ferranmar00@gmail.com",
        "disabled":True,
        "password":"7654321"
    }
}
def search_user(username:str):
    if username in users_db:
        return UserDB(users_db[username])