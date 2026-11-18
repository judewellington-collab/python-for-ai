class Dog:
    def __init__(self,name):
        self.name=name

    def bark(self):
        print(f"{self.name} is Barking!")

dog1 = Dog(name="Tom")
dog2 = Dog(name="Hutch")


print(dog1.name)
dog1.bark()

print(dog2.name)
dog2.bark()