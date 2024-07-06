# dictionaries are mutable data structures that allow you to store key-value pairs. Dictionary can be created using the dict() constructor or curly braces' {}'. Once you have created a dictionary, you can add, remove, or update elements using the methods dict. update(), dict. pop(), and dict.


customer = {
    "name" : "Aminul Islam",
    "age" : 25,
    "is_verified" : False
}


customer["name"] = "Kala Vai"  # get everywhere Kala Vai

print(customer["name"])             # Aminul Islam
print(customer["birth_date"])       # KeyError: 'birth_date'
print(customer.get("name"))         # Aminul Islam
print(customer.get("birth_date"))   # None
print(customer.get("birth_date", "05/01/2002"))  # 05/01/2002