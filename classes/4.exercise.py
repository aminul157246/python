class Person:
    def __init__(self , name):
        self.name = name
    def talk(self):
        print(f'Hi I am {self.name}')

take_person_name = Person("John Smith")
print(take_person_name.name)
take_person_name.talk()
