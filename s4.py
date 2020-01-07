class Class1: # Базовый класс
    x = 10
    def func1(self):
        print("Метод func1() класса Class1")
    def func2(self):
        print("Метод func2() класса Class1")

class Class2(Class1): # Класс Class2 наследует класс Class1
    def func3(self):
        print("Метод func3() класса Class2")

c = Class2() # Создаем экземпляр класса Class2
c.func1() # Выведет: Метод func1() базового класса Class1
c.func2() # Выведет: Метод func2() базового класса Class1
c.func3() # Выведет: Метод func3() "своего" класса Class2

print(c.x) # Обращение к атрибуту базоаого класса Class1
print(c.__dict__)
