

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.




class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):  # Dog inherit from Mammal
    # pass        # nothing to do for we use pass
    def bark(self):
        print('barking!')

class Cat(Mammal):  # Cat inherit from Mammal
    def mew(self):
        print("mewow!")

dog1 = Dog()
dog1.walk()   # walk
dog1.bark()   # barking!

cat1 = Cat()
cat1.walk()   # walk
cat1.mew()   # mewow!