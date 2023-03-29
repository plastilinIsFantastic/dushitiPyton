class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print(f'New born {self.__class__.__name__}!')
    
    def speak(self):
        print(f'It\'s {self.name}: {self.age} old')

class Cat(Animal):
    def meow(self):
        print('Meow Meow Meow')

class Dog(Animal):
    def gav(self):
        print('Woof Woof Woof')

Cat("kitty", 2).meow()

dog = Dog("puppy", 1)
dog.speak()