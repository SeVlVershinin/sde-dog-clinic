from typing import List
from fastapi import FastAPI, Query, HTTPException, Body

from data.repositories import DogRepo, PostRepo
from data.models import Dog, DogType, Timestamp

app = FastAPI(
    title='FastAPI',
    version='0.1.0',
)

dog_repo = DogRepo({
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
})

post_repo = PostRepo([
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
])


@app.get('/')
def root():
    return "The service is working"


@app.get('/dog', response_model=List[Dog])
def get_dogs(kind: DogType = Query(default=None)) -> List[Dog]:
    return dog_repo.get_dogs_by_type(kind)


@app.post('/dog', response_model=Dog)
def create_dog(dog: Dog = Body()) -> Dog:
    if dog_repo.dog_exists(dog.pk):
        raise HTTPException(status_code=409,
                            detail=f'The deg with PK {dog.pk} already exists')

    return dog_repo.create_dog(dog)


@app.get('/dog/{pk}', response_model=Dog)
def get_dog_by_pk(pk: int) -> Dog:
    if not dog_repo.dog_exists(pk):
        raise HTTPException(status_code=404,
                            detail=f'The dog with PK {pk} is not found.')

    return dog_repo.get_dogs_by_pk(pk)


@app.patch('/dog/{pk}', response_model=Dog)
def update_dog(pk: int, dog: Dog = Body()) -> Dog:
    if pk != dog.pk:
        raise HTTPException(status_code=422,
                            detail="Dog's PK can't be changed. The pk parameter must be equal to the dog's pk value")

    if not dog_repo.dog_exists(pk):
        raise HTTPException(status_code=404,
                            detail=f'The dog with PK {pk} is not found.')

    return dog_repo.update_dog(dog)


@app.post('/post', response_model=Timestamp)
def get_post() -> Timestamp:
    return post_repo.create_and_get_new_post()
