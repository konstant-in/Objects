'''
Python 3.2 +

Разрешено удаление имени из локального пространства имён, если оно используется во вложенном блоке
как несвязанное(не было определено в рамках того же блока).Ранее в таких случаях возбуждалось SyntaxError
'''
def print_done():
    some = 'some'

    del some

    # До Python 3.2 в подобных случаях инструкция вызывает SyntaxError
    # can not delete variable 'some' referenced in nested scope

    def print_some():
        print(some)

    print('done')


print_done()
