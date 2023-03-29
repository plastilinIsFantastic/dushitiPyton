class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'It\'s {self.name}: {self.age} old')

class Cat(Animal):
    def speak(self):
        print(f'Kitten says Meow! It\'s name: {self.name}, old: {self.age}')

class Dog(Animal):
    def speak(self):
        print(f'Doogo says Woof! It\'s name: {self.name}, old: {self.age}')

cat = Cat("kitty", 2)
cat.speak()

dog = Dog("puppy", 1)
dog.speak()