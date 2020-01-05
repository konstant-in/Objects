class Person:
    def __init__(self, name, age):
        """
        obj = Person('Sarah', 25)
        создаст объект obj.
        Каждому объекту можно задавать свои значения атрибутов
        obj.name == 'Sarah'
        obj.age == 25
        """
        self.name = name
        self.age = age

    @classmethod
    def add(cls, n, t):
        obj = cls(n + "+", t + 10)  # cls - подменяется идентификатором класса
        return obj


person1 = Person('Sarah', 25)
person2 = Person.add('Roark', 25)

print(person1.name, person1.age)
print(person2.name, person2.age)

person1.age = 50
person1.x = 100
person1.y = 200
print(person1.name, person1.age, person1.x, person1.y)
