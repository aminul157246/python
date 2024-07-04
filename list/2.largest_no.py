numbers = [1,2,3,4]

# largest number 
max = numbers[0]

for number in numbers:
    if(number > max):
        max = number
print(max)   # 4 


# smallest number 
min = numbers[0]

for number in numbers:
    if(number < min):
        min = number
print(min)   # 1