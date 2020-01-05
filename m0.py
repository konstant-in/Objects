class MyClass:
    x = 0

    def show(self):  # через пераметр "self" реализуется доступ к объекту "экзумпляр класса" (название может быть любым)
        print("экземплярная:", self.x, self, self.__class__)

    @classmethod      # этот декаратор говорит, что первый параметр это ссылка на объект-класс
    def show_c(cls):  # через пераметр "cls" реализуется доступ к объекту "класса" (название может быть любым)
        print("классовая   :", cls.x, cls)

    @staticmethod
    def show_s():  # не имеет доступа ни к ссылке на класс, ни к ссылке на объект
        print("статическая")


obj1 = MyClass()  # Здесь скобки обязательны, иначе создается не экземпляр класса, а новая ссылка на тот-же класс!
obj2 = MyClass()

MyClass.show(obj1)  # obj1.show()  [вторая запись более короткая, но первая лучше отражает смысл]
MyClass.show(obj2)  # obj2.show()
MyClass.show_c()    # obj1.show_c() или obj2.show_c()
MyClass.show_s()    # obj1.show_s("Hello") или obj2.show_s("Hello")

MyClass.x, obj1.x, obj2.x = 10, 1, 2

MyClass.show(obj1)  # obj1.show()
MyClass.show(obj2)  # obj2.show()
MyClass.show_c()    # obj1.show_c() или obj2.show_c()
MyClass.show_s()    # obj1.show_s("Hello") или obj2.show_s("Hello")
