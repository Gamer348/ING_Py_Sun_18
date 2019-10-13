temp = "Hello world"

temp2 = list(temp)
print(temp2)

print(ord('@'))
print(ord('H'), ord('h'))
print( 'h' > 'H')
# Задача
# Пользователь вводит произвольную строку.
# Задача - вывести средний байт-кот от всех символов в строке.

# Пример:
# @@@                                                     64

test_string = input()
temp_list = []

for i in range(0,len(test_string)):
    temp_list.append(ord(test_string[i]))

i = 0
while i < len(test_string):
    temp_list.append(ord(test_string[i]))
    i = i + 1


print(sum(temp_list)/len(temp_list))

