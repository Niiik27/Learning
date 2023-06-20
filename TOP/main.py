def sum_or_mull(num_1,num_2,num_3,operation):
    if operation == "+":
        return f"Сумма чисел = {num_1+num_2+num_3}"
    elif operation == "*":
        return f"Произведение чисел = {num_1*num_2*num_3}"
    else:
        return "Не верная команда"

print ("Задача 1 - найти сумму или произведение трех чисел")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
operation = input("Что бы перемножить введите \"*\", что бы сложить введите \"+\" ")
print(sum_or_mull(num_1,num_2,num_3,operation))



def min_max_aver(num_1,num_2,num_3,operation):
    if operation == "1":
        return f"Минимальное число = {min(num_1,num_2,num_3)}"
    elif operation == "2":
        return f"Максимальное число = {max(num_1,num_2,num_3)}"
    elif operation == "3":
        return f"Среднее арифметическое = {round((num_1+num_2+num_3)/3,6)}"
    else:
        return "Не верная команда"
    
    
print ("Задача 2 - найти минимум, максимум или среднее")
print(min_max_aver(int(input("Введите первое число: ")),
                   int(input("Введите второе число: ")),
                   int(input("Введите третье число: ")),
                   input("Выберите операцию:\n1 - min\n2 - max\n3 - average\n> ")))

def converter(meters,convert):
    if convert == 'm':
        result = meters/1609.344
        convert = "миль"
    elif convert == 'i':
        result = meters/2.54*100
        convert = "дюймов"
    elif convert == 'y':
        result = meters/0.9144
        convert = "ярдов"
    elif convert == 'f':
        result = meters/0.3048
        convert = "футов"
    else:
        print(f"Ошибка в выборе единицы измерения")
    return f"Результат {result} {convert}"
print("Задача 3 - перевести метры в мили, дюймы, ярды")
print(converter(float(input("Введите метры ")),
                input("Введите m - для перевода в мили, i - в дюймы, y - ярды, f - в футы ")
                ))

exit(0)

myInfo = {

}

def regName(arr, newName):
    arr["myName"] = newName
    return arr

def regGender(arr):
    x = int(input("1=м\n2-ж\n"))
    if x == 1:
        arr["myGender"] = "М"
    elif x == 2:
        arr["myGender"] = "Ж"
    return arr



def globalReg(arr):
    regName(arr, input("Ваше имя: "))
    regGender(arr)
    globalReg(arr)
    return arr

newInfo = globalReg(myInfo)
print(newInfo)



