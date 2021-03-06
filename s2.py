# Неросредственно перед уничтожением объекта автоматически вызывается его метод __del__(), называемый деструктором.
class MyClass:
    def __init__(self): # Конструктор класса
        print("Создан объект:", self)
    def __del__(self): # Деструктор класса
        print("Вызван метод __del__(), для:", self)


c1 = MyClass()
c2 = MyClass()
print('Конец программы')
# Обратите внимание, что метод __del__() вызывается уже после выполнения кода программы,
# после того как сборщик мусора начинает удаляють объекты
