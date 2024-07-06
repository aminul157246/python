class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    # pass        # nothing to do for we use pass
    def bark(self):
        print('barking!')

class Cat(Mammal):
    def mew(self):
        print("mewow!")

dog1 = Dog()
dog1.walk()   # walk
dog1.bark()   # barking!

cat1 = Cat()
cat1.walk()   # walk
cat1.mew()   # mewow!