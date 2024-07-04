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