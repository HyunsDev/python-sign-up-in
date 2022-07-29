from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from signin import signIn
from signup import signUp
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [ '*' ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

class LoginItem(BaseModel):
    id: str
    password: str

@app.post("/login")
def login(Item: LoginItem):
    return signIn(Item.id, Item.password)


class SignUpItem(BaseModel):
    id: str
    password: str

@app.post("/signup")
def signup(Item: SignUpItem):
    return signUp(Item.id, Item.password)