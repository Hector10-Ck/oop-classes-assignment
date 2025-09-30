# polymorphism_animals.py

class Animal:
    def move(self):
        print("Animal is moving...")

class Dog(Animal):
    def move(self):
        print("🐕 The dog is running!")

class Fish(Animal):
    def move(self):
        print("🐠 The fish is swimming!")

class Bird(Animal):
    def move(self):
        print("🐦 The bird is flying!")


# 🧪 Polymorphism demo
animals = [Dog(), Fish(), Bird()]

for animal in animals:
    animal.move()  # Same method name, different behavior
