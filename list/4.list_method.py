numbers = [2,5,6,6,4]

numbers.append(12)      # [2, 5, 6, 6, 4, 12]
numbers.insert(0, 15)   # [15, 2, 5, 6, 6, 4,]
numbers.remove(4)       # [ 2, 5, 6, 6]
numbers.clear()         # []
numbers.pop()           # [2, 5, 6, 6]
numbers.sort()          # [2, 4, 5, 6, 6]
numbers.reverse()       # [4, 6, 6, 5, 2]
print(numbers.index(6)) # 2
print(numbers.count(6)) # 2

print(numbers)            