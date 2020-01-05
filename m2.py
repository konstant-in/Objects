class Person:
    # Создание экземпляра класса с помощью конструктора
    # Person('Sarah', 25) - у данного класса два параметра конструктора
    # Конструктор - метод с именем __init__
    def __init__(self, name, age):
        # параметры конструктора (name, age) могут как-то обрабатываться
        # у нас параметры конструктора сразу присваиваются атрибутам экзеспляра класса
        self.name = name
        self.age = age


person1 = Person('Sarah', 25)
person2 = Person('Rik', 20)

person1.x = 100
person2.x = 200

print(person1, person1.name, person1.age, person1.x)
print(person1, person2.name, person2.age, person2.x)
