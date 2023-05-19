# start_number = int(input("Введите двузначное число: "))


# a=start_number//100
# print(a)
# b=start_number//10%10
# print(b)
# c=start_number%10%10%10
# print(c)

# print("Итого: "+str(a+b+c))



# start_number = int(input("Введите двузначное число: "))
# next_number=start_number
# sum=0
# k=100
# x=next_number//k
# next_number=start_number%k
# sum=sum+x
# print(x)

# k=int(k/10)
# x=next_number//k
# next_number=start_number%k
# sum=sum+x
# print(x)

# k=int(k/10)
# x=next_number//k
# next_number=start_number%k
# sum=sum+x
# print(x)
# print("Итого: "+str(sum))



# first_number = input("Введите первое число: ")
# second_number = input("Введите второе число: ")
# num=int(first_number+second_number)
# print(num)



# celsi = float(input("Введите температуру: "))
# farengeit = celsi*9/5+32
# print(farengeit)





# score=0
# test_answer = "q"
# print("Вопрос 1")
# q1 = input("Зимой и летом одним цветом?\n")
# breakpoint = input(f"Проверяемое значение = {q1}\nвведите необходимое, или пропстите - клавиша S\n")
# if breakpoint !="s":
#     q1=breakpoint
# else:
#     pass




# if q1 == "елка" or q1 == "ёлка" or q1 == "Елка" or q1 == "Ёлка" or q1 == test_answer:
#     print("Овет верный!\n")
#     score = score + 1
# else:
#     print("Подумай еще!\n")
#     score = score - 1
# print("Ваши очки: "+str(score)+"\n")
# print("Вопрос 2")
# q2 = input("Два кольца два конца, а по середине гвоздик?\n")
# if q2 == "ножницы" or q2 == "Ножницы" or q2 == test_answer:
#     print("Овет верный!\n")
#     score = score + 1
# else:
#     print("Подумай еще!\n")
#     score = score - 1
# print("Ваши очки: " + str(score) + "\n")
# print("Вопрос 3")
# q3 = input("Чем больше из нее берешь тем болше она становится?\n")
# if q3 == "яма" or q3 == test_answer:
#     print("Овет верный!\n")
#     score = score + 1
# else:
#     print("Подумай еще!\n")
#     score = score - 1
# print("Ваши очки: "+str(score)+"\n")
# print("Вопрос 4")
# q4 = input("Шел охотник по городу, увидел часы, выстрелил. Куда попал?\n")
# if q4 == "в тюрьму" or q4 == test_answer:
#     print("Овет верный!\n")
#     score = score + 1
# else:
#     print("Подумай еще!\n")
#     score = score - 1
# print("Ваши очки: " + str(score) + "\n")
# print("Вопрос 5")
# q5 = input("Какую ленту нельзя вплести в голову?\n")
# if q5 == "пулеметную" or q5 == test_answer:
#     print("Овет верный!\n")
#     score = score + 1
# else:
#     print("Подумай еще!\n")
#     score = score - 1
# print("Ваши очки: " + str(score) + "\n")

# if score >= 3:
#     q6 = input("Хотите сыграть в суперигру?\n")
#     if q6 == "нет" or q6 == "n":
#         print(f"Вы набрали {score} очка(ов)")
#     elif q6 == "да" or q6 == "y" or q6 == test_answer:
#         q7 = input("Летели два крокодила, один зеленый, другой направо. Сколько лап у ежа?\n")
#         if q7 == "4" or q7 == test_answer:
#             print("Вы выиграли!!!\n")
#             score = score ** score
#         else:
#             print("Вы все проиграли!\n")
#             score = 0
# print("Ваши очки: " + str(score) + "\n")



first = float(input("Первое число\n"))
action = input("Действие\n")
second = float(input("Второе число\n"))


if action == "+":
    result = first + second
elif action == "-":
    result = first - second
elif action == "*":
    result = first * second
elif action == "/": 
    result = first / second
elif action == "aver": 
    result = (first + second)/2
elif action == "^": 
    result = first ** second
else:
    print("Еще не умею")
if int(result)-result == 0: result = int(result)
print(f"Результат {result}")