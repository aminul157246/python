
# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.



# Think of a class as a recipe and an instance as the actual dish you make from that recipe. The class (recipe) gives you the instructions and ingredients, and the instance (dish) is the result you get when you follow the recipe.

# Here's how it breaks down:

# Class (Recipe): It defines what ingredients you need and the steps to make the dish.
# Instance (Dish): It's the actual food you prepare using the recipe.
# For example, if you have a recipe for making cookies, the recipe tells you what ingredients to use (flour, sugar, eggs, etc.) and the steps to follow (mix, bake, etc.). When you follow the recipe, you get actual cookies. Each batch of cookies you make is an instance of the recipe.

# In programming terms:

# The class defines the structure and behaviors (like the recipe).
# An instance is the actual object you create from the class (like the batch of cookies).






class Person:
  def __init__(self, _name, _age):
    self.name = _name
    self.age = _age
   
  def sayHi(self):
    print('Hello, my name is ' + self.name + ' and I am ' + self.age + ' years old!')
    
p1 = Person('Bob', 25)
p1.sayHi() # Prints: Hello, my name is Bob and I am 25 years old!