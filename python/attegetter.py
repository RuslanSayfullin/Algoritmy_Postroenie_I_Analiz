class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Иван', 25)

name = attrgetter('name')(person)
name_age = attrgetter('name', 'age')(person)
