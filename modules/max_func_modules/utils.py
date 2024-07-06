def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if(number > max):
            max = number
    return max

# numbers = [1,2,4,5]
# print(find_max(numbers))
        