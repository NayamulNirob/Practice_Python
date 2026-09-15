class Animal:
    def __init__(self):
        print("Animal")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog")

shepard = Dog()