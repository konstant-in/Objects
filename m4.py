from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def add(cls, name, year):
        obj = cls(name, date.today().year - year)
        return obj

    @staticmethod
    def is_adult(age):
        return age > 18


person1 = Person('Sarah', 25)
person2 = Person.add('Roark', 2003)

print(person1.name, person1.age)
print(person2.name, person2.age)

print(Person.is_adult(50))
print(Person.is_adult(10))
