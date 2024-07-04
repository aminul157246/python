course = 'Python for Beginners'
print(len(course))     # 20

print(course.upper())  # PYTHON FOR BEGINNERS
print(course.lower())  # python for beginners
print(course)        # Python for Beginners

# find ---> index 
print(course.find('P'))         # 0
print(course.find('Beginners')) # 11
print(course.find('X'))         # -1
print(course.replace('Beginners', 'Absolute Beginners'))    # Python for Absolute Beginners

# in --> boolean(T/F)
print('Python' in course)   # True