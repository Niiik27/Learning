print("Домашнее задание №3 - определить if, swith, или тренарный оператор подходит для решения задачи")
print("")
print("Упражнение №1 - определить статус по возрасту - подходит if-elif-else")
user_age = int(input("Сколько вам лет? "))
if 0 < user_age < 12:
    print("Вы ребенок")
elif 12 <= user_age < 18:
    print("Вы подросток")
elif 18 <= user_age < 60:
    print("Вы взрослый")
elif 60 <= user_age:
    print("Вы пенсионер")
else:
    print("Вас нет")
print("")


print("Упражнение №2 - вывести символ shif+цифра - подходит match/case")
pressed_key = input("Нажмити цифру на клавиатуре ")
match pressed_key:
    case "1":
        print("!")
    case "2":
        print("@")
    case "3":
        print("#")
    case "4":
        print("$")
    case "5":
        print("%")
    case "6":
        print("^")
    case "7":
        print("&")
    case "8":
        print("*")
    case "9":
        print("(")
    case "0":
        print("0")
    case _:
        print("Не та кнопка")


print("Упражнение №3 - проверить -есть ли в трехзначном числе одинаковые цифры")
pressed_key = input("Нажмити цифру на клавиатуре ")
match pressed_key:
    case "1":
        print("!")
    case "2":
        print("@")
    case "3":
        print("#")
    case "4":
        print("$")
    case "5":
        print("%")
    case "6":
        print("^")
    case "7":
        print("&")
    case "8":
        print("*")
    case "9":
        print("(")
    case "0":
        print("0")
    case _:
        print("Не та кнопка")



        