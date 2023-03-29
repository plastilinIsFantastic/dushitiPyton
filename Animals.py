class Animal():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'It\'s {self.name}: {self.age} old')

cat = Animal("cat", 10)
cat.speak()
