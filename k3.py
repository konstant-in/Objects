class Goat:
    name = 'Дуська'

    @staticmethod
    def sum(value1, value2):  # У нас все козы умеют складывать числа
        print("Я умею складывать " + str(value1) + " и " + str(value2))
        return value1 + value2

    @classmethod
    def rename(cls, name, text):
        cls.name = name
        print(text)


print(Goat.name)
Goat.rename("Зорька", "Меня назвали иначе")
print(Goat.name)

print(Goat.sum(1, 2))
print(Goat.sum(4, 8))
