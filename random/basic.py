import random

for number  in range(3):
    print(random.random())
    print(random.randint(10,20))  # range 10 -20 any three numbers  

name_list = ['john', 'smith', 'mosh']
print(random.choices(name_list))   # any one can came here