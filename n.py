# Импортируем класс date из модуля datetime:
from datetime import date

# Создадим новый объект, класса date
# Параметры конструктора:
# day = 27
# month = 10
# year = 1970
date1 = date(1970, 10, 27)  # Создаем еще один объект класса date, хранящий дату 27 октября 1970 года
print(date1, type(date1))
print(date1.day)
print(date1.month)
print(date1.year)

new = date.today()  # Метод класса today возвращает объект, класса date, хранящий текущее значение даты
print(new, type(new))

delta = new - date1  # Новый объект типа timedelta
print(delta, type(delta))
days = delta.days  # Этот объект имеет целочисленный параметр с именем days
print(days, type(days))
print(delta, type(delta))
print(delta.seconds)

t = delta.total_seconds()
