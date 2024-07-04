numbers = [2,3,4,4,5]

unique  = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)


# not in operator:

# The not in operator is used to check if an element is not present in a list (or any iterable).
# It returns True if the element is not found in the list.
# It returns False if the element is found in the list.