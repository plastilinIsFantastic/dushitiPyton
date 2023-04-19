from functools import total_ordering
import names


@total_ordering
class Animal():
  lAnimals = []

  def __init__(self, name: str, age: int, size: int = None):
    self.name = name
    self.age = age
    self.size = size
    Animal.totalNewBorn += self.__class__.__name__
    print(f'New born {self.__class__.__name__}!')

  @classmethod
  def listAnimals(cls):
    print(f'Total new born animals: {cls.lAnimals}')

  @staticmethod
  def randomName(gender='female'):
    return names.get_first_name(gender)

  def speak(self):
    print(f'It\'s {self.name}: {self.age} old')

  # functools.total_ordering
  # ==
  def __eq__(self, other):
    return self.size == other.size

  # <
  def __lt__(self, other):
    return self.size < other.size


class Cat(Animal):

  def meow(self):
    print('Meow Meow Meow')


class Dog(Animal):

  def gav(self):
    print('Woof Woof Woof')


cat = Cat(Animal.randomName(), 2, 10)

dog = Dog(Animal.randomName('male'), 1, 9)

Animal.count_newBorn()

#if cat > dog:
#    print('cat higher')
#else: print('dog higher')

#dog.size = 10
#if cat == dog:
#    print('loshadi')