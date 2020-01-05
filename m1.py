# Создание объектов двумя способами:
# 1. стандартный - Goat()
# 2. с помощью classmethod


class Goat:
    name = 'Дуська'

    @classmethod
    def rename(cls, name):
        cls.name = name
        obj = cls()
        return obj


g1 = Goat()
print(g1)

# Обращение к атрибутам класса через идентификаиор класса и объекта
# Их тождественность
print(Goat.name)
print(g1.name)

g2 = Goat.rename("Зорька")
print(g1, g1.name)
print(g2, g2.name)
# Объекты разные, но имена у всех одинаковые
