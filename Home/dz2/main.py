print("Домашняя работа №2")
print("Задание №1 - наити сумму и произведение трех чисел")
input_string = input("Введите три цифры ")
operation = input("Что бы перемножить введите \"*\", что бы сложить введите \"+\" ")
"""
Правильнее было бы использовать три инпута для ввода трех чисел,
но интереснее повторить задачу с разделением числа на состовляющие его цифры
"""


right = int(input_string) # Так назвал переменную, что бы обеспечить однотипность обработки. right - то что осталось после отделения цифры слева

order = len(input_string)-1 #Нужно знать сколько введено цифр, что бы использовать это для отделения старшей цифры
left = right//(10**order)#Здесь потребуется оператор степени, что бы задать нужное количество нулей после единицы
right = right%(10**order)# Число преобразует само себя. Это позволит без модификации повторять код столько раз, сколько потребуется
result = left
# print('left', left)
# print('right', right)

"""Вот повторяемый блок кода"""
order = order-1
left = right//(10**order)#Текущая рабочая цифра - требуется ее перемножить или сложить с остальными цифрами
right = right%(10**order)#Текущий набор цифр


if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass


# print('left', left)
# print('right', right)

order = order-1
left = right//(10**order)
right = right%(10**order)

if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass
print("")
# print('left', left)
# print('right', right)

print(f"Результат {result}")
print("")

"""Небольшая модификация под числа большей разрядности(но одинаковые по разряду)"""
print("")
print("Модификация")
input_string = input("Введите три числа ")
input_len_num = int(input("Сколькизначные числа? "))
operation = input("Что бы перемножить введите \"*\", что бы сложить введите \"+\" ")

right = int(input_string) # Так назвал переменную, что бы обеспечить однотипность обработки. right - то что осталось после отделения цифры слева

order = len(input_string)-input_len_num #Нужно знать сколько введено цифр, что бы использовать это для отделения старшей цифры
left = right//(10**order)#Здесь потребуется оператор степени, что бы задать нужное количество нулей после единицы
right = right%(10**order)# Число преобразует само себя. Это позволит без модификации повторять код столько раз, сколько потребуется
result = left
# print('left', left)
# print('right', right)

"""Вот повторяемый блок кода"""
order = order-input_len_num
left = right//(10**order)#Текущая рабочая цифра - требуется ее перемножить или сложить с остальными цифрами
right = right%(10**order)#Текущий набор цифр


if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass


# print('left', left)
# print('right', right)

order = order-input_len_num
left = right//(10**order)
right = right%(10**order)

if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass
print("")
# print('left', left)
# print('right', right)

print(f"Результат {result}")
print("")

"""Еще небольшая модификация под числа большей разрядности(но одинаковые по разряду) с автоопределением разрядности"""
print("")
print("Модификация 2")
input_string = input("Введите числа ")

operation = input("Что бы перемножить введите \"*\", что бы сложить введите \"+\" ")

right = int(input_string)

input_len_num = int((len(input_string)+1)//3)  #если ввести неполное число, то оно должно дополниться нулем. почему то иногда флоат случался. по этому приведение к инту


order = len(input_string)-input_len_num 
left = right//(10**order)
right = right%(10**order)
result = left
# print('left', left)
# print('right', right)

"""Вот повторяемый блок кода"""
order = order-input_len_num
left = right//(10**order)#Текущая рабочая цифра - требуется ее перемножить или сложить с остальными цифрами
right = right%(10**order)#Текущий набор цифр


if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass


# print('left', left)
# print('right', right)

order = order-input_len_num
left = right//(10**order)
right = right%(10**order)

if operation=="!":
    result = result * left
elif operation=="+":
    result = result + left
else:
    pass
print("")
# print('left', left)
# print('right', right)

print(f"Результат {result}")




print("")
print("Задание №2 - максимум, минимум или среднее из трех чисел")
first = int(input("Первое число "))
second = int(input("Второе число "))
third = int(input("Третье число "))
operation = input("max or min or average ")
"""
С разделением числа наигрался, по этому теперь будет просто ввод чисел
"""
if operation == "average":
    result = (first+second+third)/3
    print(f"Среднее арефметическое равно {result}")
elif operation == "max":
    maximum = first
    if maximum < second: maximum = second
    if maximum < third: maximum = third
    print(f"Максимум равен {maximum}")
elif operation == "min":
    minimum = first
    if minimum > second: minimum = second
    if minimum > third: minimum = third
    print(f"Минимум равен {minimum}")
else:
    print("Ошибка в выбранном действии")


"""
В процессе написания - названия переменных совпадали с операторами, и вылазили подсказки. По этому решил из опробовать
"""
print("")
print("Задание №2 - максимум, минимум или среднее из трех чисел")
first = int(input("Первое число "))
second = int(input("Второе число "))
third = int(input("Третье число "))
operation = input("max or min or average ")
if operation == "average":
    result = (first+second+third)/3
    aver
    print(f"Среднее арефметическое равно {result}")
elif operation == "max":
    maximum = max(first,second,third)
    print(f"Максимум равен {maximum}")
elif operation == "min":
    minimum = min(first,second,third)
    print(f"Минимум равен {minimum}")
else:
    print("Ошибка в выбранном действии")



print("")
print("Задание №3 - перевести метры в мили, дюймы, ярды")
meters = float(input("Введите метры "))
convert = input("Введите m - для перевода в мили, i - в дюймы, y - ярды, f - в футы ")
if convert == 'm':
    result = meters/1609.344
elif convert == 'i':
    result = meters/2.54*100
elif convert == 'y':
    result = meters/0.9144
elif convert == 'f':
    result = meters/0.3048
else:
    print(f"Ошибка в выборе единицы измерения")
print(f"Результат {result}")