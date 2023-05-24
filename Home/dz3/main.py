

"""
В задании было разрешено использовать разные виды условных операторов. Те что не проходили - погуглил и применил.
Оператор match/case появился в 3.10 версии - значит можно пользоваться
так же попался оператор инкримента/декремента - его тоже стал использовать
и пришлось отыскать функцию выхода из приложения, что бы не коментить предыдущие задания, а недлопускать их к выполнению
что бы не наслоились коментарии к коду на закоментирование целого блока
теперь текущую задачу выполняю вначале кода, а после задачи сьавлю exit, когда задача решена - копипастю ее на свое место
"""


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


print("Упражнение №3 - проверить -есть ли в трехзначном числе одинаковые цифры - подойдет тренарный оператор")

input_string = input("Введите трехзначное число ")
num = int(input_string)


order = len(input_string)-1
first = num//(10**order)
num = num%(10**order)

order = order-1
second = num//(10**order)
num = num%(10**order)

order = order-1
third = num//(10**order)
num = num%(10**order)

result = "Нет повторяющихся цифр" if first!=second!=third else "Есть повторения"
print("")
print(result)
print("")

print("Упражнение №4 - определить - является ли год високосным - подходит if-elif-else")
year=int(input("Введите год "))
if year%400==0:
    print("Високосный")
elif year%100==0:
    print("Обычный")
elif year%4==0:
    print("Високосный")
else:
    print("Обычный")


"""Пока не понятно что больше подойдет, но уже все операторы сравнения использованы, по этому - любой способ
Нужно сравнивать крайние символы слева и справа. Либо если половина строки == второй половине наоборот, то это  палиндром. Получение левого числа - освоено.
теперь нужен алгоритм для правого числа, либо разобрать число по цифрам - оно не большое"""

print("Упражнение №5 - проверить число на палиндром")
input_string = input("Введите пятизначное число ")
num = int(input_string)


order = len(input_string)-1
first_right = num - num//10*10
print("first_right",first_right)
first_left = num//(10**order)
num = num%(10**order)//10
order = order-1
print(num)

if first_right == first_left:
    order = order-1
    first_right = num - num//10*10
    print("first_right",first_right)
    first_left = num//(10**order)
    num = num%(10**order)//10
    order = order-1#Теперь число теряет по 2 цифры
    print(num)
    if first_right == first_left:
        order = order-1
        first_right = num - num//10*10
        print("first_right",first_right)
        first_left = num//(10**order)
        num = num%(10**order)//10
        order = order-1
        print(num)
        if first_right == first_left:
            result = "Это ПАЛИНДРОМ!"#в пятизначном числе есть средняя цифра и по бокам по две цифры. Значит на втором сравнении плечи закончатся
        else:
            result = "Это не плалиндром!"
    else:
        result = "Это не плалиндром!"
else:
    result = "Это не плалиндром!"

print("")
print(result)
print("")
    
    
    
"""Тут врове все просто - коментировать особо нечего"""    
print("Упражнение №6 - Сконвертировать доллар в другую валюту")
usd = float(input("Введите сумму в долларах "))
money = input("Во что конвертировать - EUR, UAN, AZN, RU(По умолчанию)? ")
result =  0.0
match money:
    case "":
        money = "RU"
        result =  usd*80.17
    case "EUR":
        result =  usd*0.92764
    case "UAN":
        result =  usd*7.06
    case "AZN":
        result =  usd*1.7
    case "RU":
        result =  usd*80.17
    case _:
        print(f"В {money} не конвертирую")
        result =  usd
        money = "USD"
        
print(f"{usd} USD = {result} {money}")




#match/case - не подойдет так как в case можно только эталон указывать, тренарный тоже не пойдет - много условий
print("Упражнение №7 - Сделать скидку")
money = float(input("Введите сумму покупки "))

if 0 < money < 200:
    discount = 0
elif 200 <= money < 300:
    discount = 3
elif 300 <= money < 500:
    discount = 5
elif 500 <= money:
    discount = 7
else:
    print("Введите положительное число")
    discount = 0
print("")
     
money = money - (money/100*discount)
        
print(f"Цена со скидкой = {money} рублей")


#Тренарный оператор
print("Упражнение №8 - Узнать впишется ли окружность в квадрат ")
ring_len = float(input("Введите длину окружности "))
perimeter = float(input("Введите периметр квадрата "))
d = ring_len/(2*3.141592) 
side = perimeter/4
result = "помещается" if d<=side else "слишком большая!"
print(f"Окружность {result}")


"""Здесь просто if Все условия индивидуальны и должны проверяться внезависимости друг от друга, а результат нужен только один, все неверные ответы можно либо проигнорировать,
либо как то по желанию оформить
"""

print("Упражнение №9 - Спросить пользователя и наградить за верный ответ ")
q_1 = input("Сколько грамм в килограмме - 100, 1000, 900? ")

score = 0
nxt=' '
if q_1=="1000":
    score+=2
    print("Молодец! Вам 2 очка")
    nxt=' еще '
else:
    print("Ответ неверный!")
print(f"У вас {score} очк.")



q_2 = input("Спутник Земли - Луна, Марс, Юпитер? ")
if q_2=="Луна" or q_2=="луна":
    score+=2
    print(f"Молодец! Вам{nxt}2 очка")
    nxt=' еще '
else:
    print("Ответ неверный!")
print(f"У вас {score} очк.")


q_3 = input("Драгоценный метал - Медь, Аллюминий, Серебро? ")
if q_3=="Серебро" or q_3=="серебро":
    score+=2
    print(f"Молодец! Вам{nxt}2 очка")
else:
    print("Ответ неверный!")

print(f"Вы набрали {score} очк.")





print("Упражнение №10 - Показать следующий день ")
current_day = int(input("Введите день "))
current_month = input("Введите месяц ")

match current_month:
    case "январь":
        current_month = 1
    case "февраль":
        current_month = 2    
    case "март":
        current_month = 3
    case "апрель":
        current_month = 4
    case "май":
        current_month = 5
    case "июнь":
        current_month = 6    
    case "июль":
        current_month = 7
    case "август":
        current_month = 8 
    case "сентябрь":
        current_month = 9
    case "октябрь":
        current_month = 10    
    case "ноябрь":
        current_month = 11
    case "декабрь":
        current_month = 12   
    case _:
        current_month = int(current_month)
        if current_month > 12:
            current_month=12    
      
        
current_yaer = int(input("Введите год "))

month_31 = (bool(current_month%2) and current_month < 8) or (bool(current_month%2==0) and current_month > 7)


if month_31:
    if current_month == 12:
        if current_day>30:#Если кто то введет дату больше 31 то она будет расценена как 31
            current_yaer+=1
            current_month=1
            current_day=1
        else:
            current_day+=1
    elif current_day>30:#Если кто то введет дату больше 31 то она будет расценена как 31
        current_month+=1
        current_day=1
    else:
        current_day+=1
else:
    if current_month==2:

        if current_yaer %400==0:
            leap=1
        elif current_yaer %100==0:
            leap=0
        elif current_yaer %4==0:
            leap=1
        else:
            leap=0

        if current_day>27+leap:#Если кто то введет дату больше 28/29 то она будет расценена как 28/29 
            current_month+=1
            current_day=1
        else:
            current_day+=1
    elif current_day>29:#Если кто то введет дату больше 30 то она будет расценена как 30
            current_month+=1
            current_day=1
    else:
        current_day+=1




match current_month:
    case 1:
        current_month = "Январь"
    case 2:
        current_month = "Февраль"    
    case 3:
        current_month = "Март"
    case 4:
        current_month = "Апрель"
    case 5:
        current_month = "Май"
    case 6:
        current_month = "Июнь"  
    case 7:
        current_month = "Июль"
    case 8:
        current_month = "Август" 
    case 9:
        current_month = "Сентябрь"
    case 10:
        current_month = "Октябрь"   
    case 11:
        current_month = "Ноябрь"
    case 12:
        current_month = "Декабрь"   
    # case _:
    #     current_month = int(current_month) 

print(f"Следующий день будет: {current_day}, {current_month}, {current_yaer} г.")





exit(0)