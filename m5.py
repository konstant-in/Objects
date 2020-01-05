class ToyClass:
    def method_i(self, value1, value2):  # instance method
        return value1, value2, self

    @classmethod
    def method_c(cls, value1, value2):  # class method
        return value1, value2, cls

    @staticmethod
    def method_s(value1, value2):  # static method
        return value1, value2


obj = ToyClass()

# Все типы методов можно вызывать используя либо идентификатор класса, либо идентивикатор объекта
v_method_i = ToyClass.method_i(obj, 'p1', 'p2')  # идентивикатор класса (Здесь требует указывать все 3 аргумента)
v_method_i2 = obj.method_i('p1', 'p2')           # идентивикатор объекта

v_method_c = ToyClass.method_c('p1', 'p2')       # идентивикатор класса
v_method_c2 = obj.method_c('p1', 'p2')           # идентивикатор объекта

v_method_s = ToyClass.method_s('p1', 'p2')       # идентивикатор класса
v_method_s2 = obj.method_s('p1', 'p2')           # идентивикатор объекта

print(v_method_i)
print(v_method_i2)

print(v_method_c)
print(v_method_c2)

print(v_method_s)
print(v_method_s2)
