# можно дабавить свои методы
class MyClass:
    def view(self):
        # У всякого метода по крайней мере один параметр.
        # Он должен содержать ссылку на экземпляр класса
        print(self.__dir__())

c1 = MyClass()

# Два способа записи вызова метода:

# При первом способе записи вызава метода ему надо на месте первого параметра (self) передать ссылку на экземпляр этого класса.
MyClass.view(c1)
c1.x = 10
MyClass.view(c1)


# При втором способе записи вызава метода первый параметр  (self) опускается, т.к. ссылка на экземпляр класса уже задана другим способом
c1.view()
c1.y = 10
c1.view()