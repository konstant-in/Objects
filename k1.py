class MyClass:
    x = 10
    y = 20
    print("Класс MyClass создан!")


print(MyClass.x, MyClass.y)

MyClass.x = 18
MyClass.y = 34

print(MyClass.x, MyClass.y)

print(MyClass.__dict__)
print(MyClass.__base__)
print(MyClass.__bases__)
print(MyClass.__basicsize__)
print(MyClass.__dictoffset__)
print(MyClass.__flags__)
print(MyClass.__itemsize__)
print(MyClass.__mro__)
print(MyClass.__name__)
print(MyClass.__qualname__)
print(MyClass.__text_signature__)
print(MyClass.__weakrefoffset__)
print(MyClass.__doc__)
print(MyClass.__module__)
