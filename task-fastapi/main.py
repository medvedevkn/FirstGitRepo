from fastapi import FastAPI

app = FastAPI()

from enum import Enum
from pydantic import BaseModel
from typing import Union
from fastapi import Header
from fastapi import HTTPException

class DogType(str, Enum):
    terrier = 'terrier'
    bulldog = 'bulldog'
    dalmatian = 'dalmatian'

class Dog(BaseModel):
    name: str
    pk: int 
    kind: DogType

class Timestamp(BaseModel):
    id: int 
    timestamp: int

@app.get('/', status_code=200)
async def root():
    return {'message': 'Successful Response'}

@app.get('/dog', status_code=200)
async def get_dogs(kind: Union[DogType, None] = None):
    dog = Dog(name = 'string', pk = 0, kind = kind)
    return [dog]

@app.post('/post', status_code=200)
async def get_post():
    ts = Timestamp(id=0, timestamp=0)
    return ts

@app.post('/dog', status_code=200)
async def create_dog(dog: Dog):
    dog.name = 'string'
    dog.pk = 0
    dog.kind = 'terrier'
    return dog

@app.get('/dog/{pk}', status_code=200)
async def get_dog_by_pk(pk: int):
    dog = Dog(name='string', pk = pk, kind = 'terrier')
    return dog


@app.patch('/dog/{pk}', status_code=200)
async def update_dog(pk: int, dog: Dog):
    dog.pk = pk
    return dog

## на задание "Реализовано получение собак по типу - 1 балл" не увидел референса в исходном swagger.
## Просьба игнорировать, если задание неактуально
## В целом задание очень необычное, даже немного странное. Написание псевдокода напомнило времена старших классов, когда приходилось писать псевдокод на листочке 
@app.get('/dog/{type}', status_code=200)
async def get_dog_by_kind(type: DogType):
    dog = Dog(name='string', pk = 0, kind = type)
    return dog