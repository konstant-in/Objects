class Test:

    def __init__(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y
        # Этот метод автоматически выполняется всякий раз когда создается экземпляр класса
        print("Экземпляр класса создан. " + str(self))


obj1 = Test(1, 2)  # Без указания параметров x и y нельзя создать объект
# TypeError: __init__() missing 1(2) required positional argument
obj2 = Test(3, 4)
obj3 = Test(5, 6)

print(obj1.x, obj1.y)
print(obj2.x, obj2.y)
print(obj3.x, obj3.y)

# Язык допускает создание дополнотельных атрибутов, не перечисленных в конструкторе,
# но правила вежливости это запрещают
obj3.z = 7  # Так можно, но не нужно
print(obj3.x, obj3.y, obj3.z)
