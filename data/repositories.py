import random

from data.models import Dog, DogType, Timestamp


class DogRepo:
    def __init__(self, dogs_db: dict[int, Dog]):
        self._dogs_db = dogs_db

    def get_dogs_by_pk(self, pk: int) -> Dog:
        return self._dogs_db[pk]

    def get_dogs_by_type(self, dog_type: DogType = None) -> list[Dog]:
        def filter_predicate(dog: Dog) -> bool:
            if dog_type:
                return dog.kind == dog_type
            else:
                return True

        return list(filter(filter_predicate, self._dogs_db.values()))

    def dog_exists(self, pk: int | None):
        return pk in self._dogs_db

    def create_dog(self, new_dog: Dog) -> Dog:
        pk = new_dog.pk
        if pk is None:
            pk = max(self._dogs_db.keys()) + 1
        if self.dog_exists(pk):
            raise ValueError(f'A dog with pk {pk} already exists ')
        new_dog.pk = pk
        self._dogs_db[pk] = new_dog
        return new_dog

    def update_dog(self, updated_dog: Dog) -> Dog:
        pk = updated_dog.pk
        if not self.dog_exists(pk):
            raise ValueError(f'A dog with pk {pk} does not exist')
        self._dogs_db[pk] = updated_dog
        return updated_dog


class PostRepo:
    def __init__(self, post_db: list[Timestamp]):
        self._post_db = post_db

    def create_and_get_new_post(self):
        new_id = max(self._post_db, key=lambda ts: ts.id).id + 1
        new_ts = Timestamp(id=new_id, timestamp=random.randint(10, 100))
        self._post_db.append(new_ts)
        return new_ts
