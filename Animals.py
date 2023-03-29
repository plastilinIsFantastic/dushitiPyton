class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'It\'s {self.name}: {self.age} old')

class Cat(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        print('New born Cat!')
    
    def getVoice(self):
        print('Meow')

class Dog(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        print('New born Dog!')

    def getVoice(self):
        print('Meow')

cat = Cat("kitty", 2)
cat.speak()
cat.getVoice()

dog = Dog("puppy", 1)
dog.speak()