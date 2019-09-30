#1) Словарный запас +++++
#2) Грамматика (порядок слов) +
"""
I 
am 
SUPERMAN
"""

# Переменная - это?
# Переменная - минимальная область памяти, способная хранить что-либо.

# адрес и хранимое значение

a = 10 # name PRISVOIT value

#Базовые типы данных.
# 1. Целые числа (INTEGER int)

a1 = 20
b1 = 30
a1 = a1 + 20
c1 = a1 + b1
print(a1 + b1)
print(c1)

# 2. Вещественные (Числа с плавающе точкой, float)
a1 = 25.2
_a1 = 25.2
b1 = 26.39999

#3. Арифметика
print( 2 * 3)
print( 2 / 3)
print( 2**0.5)
print(10//3)
print(10%2)

print(5.0 == 5)

#4. Логический тип (Булев тип, bool)
t_bool = True  # 1
f_bool = False # 0

# Таблица истинности
print("#############################################")
print( True and True) # 1 * 1 = 1
print( True and False) # 1 * 0 = 0
print( False and True) # 0 * 1 = 0 
print( False and False) # 0 * 0 = 0

print('#####################################')

print(True + True**False)

# 5. Строки
# Строка - последовательность символов, заключенная в кавычки.
a_string = "Hello"
b_string = "World!"
print(a_string + " " + b_string)

# 6. NoneType

n = None


# 7. Жирность
print("###################################")
a = 10
print(type(a), a.__sizeof__(), a)
b = 10.234
print(type(b), b.__sizeof__(), b)
c = True
print(type(c), c.__sizeof__(), c)
d = "assdgdh"
print(type(d), d.__sizeof__(), d)
q = None
print(type(q), q.__sizeof__(), q)
print("###################################")