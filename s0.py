class MyClass:
    pass

c = MyClass()
# Класс имеет встроенные атрибуты и методы
# встроенные атрибуты можно посмотреть встроенным методом __dir__()
print(c.__dir__())

# Собственные атрибуты экземпляра можно задавать так
c.v1 = 1
c.v2 = 2
print(c.v1, c.v2)
print(c.__dir__())