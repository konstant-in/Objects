class Person:
    par = "Test"

    def __init__(self):
        """Этот метод
        автоматически вызывается при создании объектов,
        например вызове Person(),
        и создает параметры и инициализирует их значения
        """
        self.name = None
        self.age = None


print(Person.par)  # доступ к парамертам классов, чарез идентификатор класса возможен
try:
    print(Person.name)
except:
    print('''Попытка к доступу к парамертам объектов, чарез идентификатор класса
выдает ошибку "AttributeError: type object 'Person' has no attribute 'name'"''')

person1 = Person()
person2 = Person()

person1.name = 'Tom'
person1.age = 50
person1.x = 100
person1.y = 200

person2.name = 'Jon'
person2.age = 20
person2.x = 150
person2.y = 250

print(person1.name, person1.age, person1.x, person1.y)
print(person2.name, person2.age, person2.x, person2.y)
