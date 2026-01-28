from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional



app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea]=[]

@app.get("/")
def read_root():
    return {"Hello": "codeguyakash"}

@app.get("/teas")
def get_teas():
    return teas


@app.post("/teas")
def create_tea(tea: Tea):
    teas.append(tea)
    return tea



