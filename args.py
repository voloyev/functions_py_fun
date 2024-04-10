person = {'name': "Bob", 'age': 22}

def change_name(person=person):
    person['name'] = 'Alice'


change_name()
print(person)
# >>> {'name': 'Alice', 'age': 22}
