try:
    age = int(input("Age : "))
    
    income = 30
    risk = income / age
    print(age)
    
except ZeroDivisionError:
    print('cannot divided by 0!')
except ValueError:
    print('invalid value!')

