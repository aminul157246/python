def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}")

greet_user("John","Doe")
    
# keyword argument / position of argument
greet_user("Doe", "John")     # Doe John
greet_user(last_name="Doe", first_name="John")  # John Doe

# we use keyword argument for readability of code 

