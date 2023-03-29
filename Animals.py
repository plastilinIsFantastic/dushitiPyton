class Animal():
    def __init__(self, name: str, age: int, size: int = None):
        self.name = name
        self.age = age
        self.size = size
        print(f'New born {self.__class__.__name__}!')
    
    def speak(self):
        print(f'It\'s {self.name}: {self.age} old')

    # magic mikey, noo it are magic compare methods
    # <
    def __lt__(self, other):
        return self.size < other.size
    # >
    def __gt__(self, other):
        return self.size > other.size
    # ==
    def __eq__(self, other):
        return self.size == other.size
    # >=
    def __le__(self, other):
        return self.size <= other.size
    # <=
    def __ge__(self, other):
        return self.size >= other.size
    # !=
    def __ne__(self, other):
        return self.size != other.size

class Cat(Animal):
    def meow(self):
        print('Meow Meow Meow')

class Dog(Animal):
    def gav(self):
        print('Woof Woof Woof')

cat = Cat("kitty", 2, 10)
dog = Dog("puppy", 1, 9)

if cat > dog:
    print('cat higher')
else: print('dog higher')

dog.size = 10
if cat == dog:
    print('loshadi')