# Методы класса можно использовать для задания/изменения атрибутов экземпляра класса
class MyClass:
    def initialization(self, value1, value2):
        self.v1 = value1
        self.v2 = value2

# так
c1 = MyClass()
MyClass.initialization(c1, 2, 4)

# или так
c2 = MyClass()
c2.initialization(20, 40)



print(c1.v1, c1.v2)
print(c2.v1, c2.v2)
