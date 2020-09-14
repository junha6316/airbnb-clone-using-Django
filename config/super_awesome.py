class Animal:
    def pee(self):
        print("shshshsh")


class Dog(Animal):
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I will pee")


pug = Dog()


class Puppy(Dog):
    def pee(self):
        print("go to the park")
        super().pee()


p = Puppy()
p.pee()
