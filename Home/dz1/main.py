print ("Задача 1 - найти сумму и произведение трех чисел")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
num_3 = int(input("Введите третье число: "))
sum = num_1+num_2+num_3
print("Сумма чисел = ",sum,'\n',f"Произведение чисел = {num_1*num_2*num_3}\n")

print ("Задача 2 - сколько осталось денег")
salary = float(input("Ваша зарплата: "))
credit = float(input("Выплата по кредиту: "))
payment = float(input("ЖКХ: "))
total = salary-credit-payment
print(f"Итого в остатке {total} руб.\n")

print ("Задача 3 - найти площадь ромба по диагоналям")
d1 = float(input("Введите длину первой диагонали: "))
d2 = float(input("Введите длину второй диагонали: "))
area = d1*d2/2
print("Площадь ромба равна " + str(area) + " м.кв.\n")

print ("Задача 4 - вывод надписи на разных строках")
print("To be\nor not\nto be\n")
print ("Задача 5 - вывод надписи на разных строках")
print('“Life is what happens\n\twhen\n\t\tyou’re busy making other plans”\n\t\t\t\t\tJohn Lennon.\n')
