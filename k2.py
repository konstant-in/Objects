class ToyClass:
    x = 0
    y = 0

    @staticmethod
    def method_s(var1, var2):
        pass
        # Здесь код, который выполняется при вызове метода
        # Вызов метода: ToyClass.method_s(var1, var2)
        # var1, var2 - параметры метода

    @classmethod
    def method_c(cls, var1, var2):
        pass
        # Здесь код, который выполняется при вызове метода
        # Вызов метода: ToyClass.method_c(var1, var2)
        # var1, var2 - параметры метода
        # cls - этот параметр, при вызове метода задавать не требуется; он хранит ссылку на метод класса
        # С его помощью можно, например, из кода обращаться к атрибутам класса так: cls.<атрибут класса>


