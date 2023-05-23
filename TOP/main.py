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



# first = float(input("Первое число\n"))
# action = input("Действие\n")
# second = float(input("Второе число\n"))


# if action == "+":
#     result = first + second
# elif action == "-":
#     result = first - second
# elif action == "*":
#     result = first * second
# elif action == "/": 
#     result = first / second
# elif action == "aver": 
#     result = (first + second)/2
# elif action == "^": 
#     result = first ** second
# else:
#     print("Еще не умею")
# if int(result)-result == 0: result = int(result)
# print(f"Результат {result}")

print(f"{bool(100%6)}")
print(f"{bool(100%4)}")
# year=int(input("Введите год "))



# if year%4:
#     print("Обычный")
# elif year%100:
#     print("Високосный")
# elif year%400:
#     print("Обычный")
# else:
#     print("Високосный")


# if year%400==0:
#     print("Високосный")
# elif year%100==0:
#     print("Обычный")
# elif year%4==0:
#     print("Високосный")
# else:
#     print("Обычный")

# side_a=int(input("Введите сторону А "))
# side_b=int(input("Введите сторону B "))
# side_c=int(input("Введите сторону C "))

# if side_a + side_b > side_c and side_a + side_c > side_b and side_c + side_b > side_a:
#     if side_a != side_b != side_c:
#         print("Это разносторонний треугольник")
#     elif side_a == side_b == side_c:  
#         print("Это равносторонний треугольник")
#     else:
#         print("Это равнобедренный треугольник")
# else:
#     print("Это не треугольник!")

nameGame = "Подземелья"
print("Добро пожаловать \n 'Подземелья'")


print("Выберите пол персонажа:\n", "ж-женский\n", "м-Мужской")
gender = str(input("Введите ж или м :\n"))
if gender == "М" or gender == "м":
  gender = "Мужской"
elif gender == "Ж" or gender == "ж":
  gender = "Женский"
print(f"Вы выбрали {gender} пол")

print("Выберете расу персонажа ч-человек,\n э-эльф")
race = str(input("Введите ч или э:\n"))
if race == "ч" or race == "Ч":
  race = "Человек"
elif race == "э" or race == "Э":
  race = "Эльф"
  
  print(f"Вы выбрали рассу {race}")

if race == "Человек":
  scoreRole = 0  # галочка для выбора класса
  print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
  role = input("введите 1,2,3 или 4 для выбора класса:")
  if role == "1":
    role = "Воин\n"
  elif role == "2":
    role = "Лучник\n"
  elif role == "3":
    role = "Жрец\n"
  elif role == "4":
    role = "Маг\n"

elif race == "Эльф":
    print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
          "4-Паладин\n")
    role = input("введите 1,2,3 или 4 для выбора класса")
    if role == "1":
      role = "Воин"
    elif role == "2":
      role = "Лучник"
    elif role == "3":
      role = "Темный Колдун"
    elif role == "4":
      role = "Паладин"
print(f"Вы выбрали класс:{role}")

name = str(input("Введите имя вашего персонажа"))
print("\nИнформация о персонаже:\n"
        f"пол персонажа {gender}\n"
        f"Раса персонажа {race}\n"
        f"Класс:{role}\n"
        f"Имя:{name}\n")
