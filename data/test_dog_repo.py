from unittest import TestCase
from data.repositories import DogRepo
from data.models import Dog, DogType


class TestDogRepo(TestCase):
    def setUp(self):
        self._repo = DogRepo({
            0: Dog(name='Bob', pk=0, kind='terrier'),
            1: Dog(name='Marli', pk=1, kind="bulldog"),
            2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
            3: Dog(name='Rex', pk=3, kind='dalmatian'),
            4: Dog(name='Pongo', pk=4, kind='dalmatian'),
            5: Dog(name='Tillman', pk=5, kind='bulldog'),
            6: Dog(name='Uga', pk=6, kind='bulldog')
        })

    def test_get_dogs_by_pk(self):
        dog = self._repo.get_dogs_by_pk(3)
        self.assertEqual(dog, Dog(name='Rex', pk=3, kind=DogType.dalmatian))

    def test_get_dogs_by_none_as_dog_type(self):
        dogs = self._repo.get_dogs_by_type()
        self.assertEqual(len(dogs), 7)

    def test_get_dogs_by_type(self):
        dogs = self._repo.get_dogs_by_type(DogType.terrier)
        self.assertEqual(len(dogs), 1)
        self.assertEqual(dogs[0], Dog(name='Bob', pk=0, kind=DogType.terrier))

    def test_dog_exists(self):
        self.assertTrue(self._repo.dog_exists(5))
        self.assertFalse(self._repo.dog_exists(12))
        self.assertFalse(self._repo.dog_exists(None))

    def test_create_dog(self):
        new_dog = Dog(name='Newby', kind=DogType.terrier)
        created_dog = self._repo.create_dog(new_dog)
        expected_dog = Dog(name='Newby', pk=7, kind=DogType.terrier)
        self.assertEqual(created_dog, expected_dog)

        created_dog = self._repo.get_dogs_by_pk(7)
        self.assertEqual(created_dog, expected_dog)

    def test_create_dog_with_existing_pk(self):
        new_dog = Dog(name='Newby', pk=2, kind=DogType.terrier)
        with self.assertRaises(ValueError):
            self._repo.create_dog(new_dog)

    def test_update_dog(self):
        dog_with_new_data = Dog(name='The Snoop', pk=2, kind=DogType.dalmatian)
        updated_dog = self._repo.update_dog(dog_with_new_data)
        self.assertEqual(updated_dog, Dog(name='The Snoop', pk=2, kind=DogType.dalmatian))

    def test_update_dog_that_does_not_exist(self):
        dog_with_new_data = Dog(name='The Snoop', pk=13, kind=DogType.dalmatian)
        with self.assertRaises(ValueError):
            self._repo.update_dog(dog_with_new_data)


