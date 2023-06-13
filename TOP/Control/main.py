
while True:
    registeredUsers = []
    myName = input("Введите Имя ")
    mySurName = input("Введите Фамилию ")
    myLogin = input("Введите Логин ")
    myPass = input("Введите пароль ")

    userCard = {
                "myName":myName,
                "mySurName":mySurName,
                "myLogin":myLogin,
                "myPass": myPass,         
                }
    # validLogin = False
    while True:
        validLogin = True
        for user in registeredUsers:
            if userCard["myLogin"] == user["myLogin"]:
                print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                userCard["myLogin"] = input("Такой логин уже занят. Введите другой логин ")
                validLogin = False
                break
        
        if validLogin == True: break

            
    registeredUsers.append(userCard)


exit(0)



from datetime import date
current_date = date.today()
currentDate = str(current_date).split("-")
print(currentDate)

print("Задание №1 - Карточка пользователя:")

myName = input("Введите Имя ")
mySurName = input("Введите Фамилию ")
# myAge = int(input("Введите Возраст "))
myBirth = input("Введите дату рождения в формате ДД.ММ.ГГГГ ")
birthDate = myBirth.split(".")
myAge = int(currentDate[0])-int(birthDate[2])

if (birthDate[1])>(currentDate[1]):
    myAge-=1
print(myAge)
userCard = {
            "myName":myName,
            "mySurName":mySurName,
            "myAge":myAge,
            "myBirth": myBirth,         
            }
print(f"Имя пользователя: {userCard['myName']}\nФамилия пользователя: {userCard['mySurName']}\nВозраст пользователя: {userCard['myAge']} лет\nДень рождения пользователя: {userCard['myBirth']} г.\n")
print("--------------------------------------------------------")
print("Задание №2 - Выбрать загадку:")


#Объектом интересней - так как ввод может быть - на лево, на право, прямо, но писать сложно,
# по этому ключи будут 1,2,3, а в будущем можно будет из заменить на что то более разговорное
riddles = {
    "1": "Висит груша нельзя скушать? ",
    "2": "Два кольца два конца, по середине гвоздик? ",
    "3": "Что больше слона, и ни чего не весит? "
}

responses = {
    "1": "лампочка",
    "2": "ножницы",
    "3": "тень"
}

# riddles.items - это массивчики, содержащие ключ[0],значение[1]
# смотрел в его сторону но не пригодилось
str_riddles = ""
for key in riddles:# При обходе словаря в цикле в key возвращается значение ключа
    str_riddles += f"{key} - {riddles[key]}\n"
way = input(f"Выберите загадку:\n{str_riddles}")
print(riddles[way])


try_count = 3
win = False
while try_count>0:
    response = input(f"Ответ на загадку (у вас {try_count} попытки): ")
    try_count-=1
    if response == responses[way]:
        print("Верно!")
        win = True
        break
    else:
        print(f"Попробуйте еще раз, осталось {try_count} попытки")

if win:
    print("Поздравляем!")
else:
    print("Вы проиграли")


import random
print("Задание №3 - Угадай число")
secret_int = random.randint(0,10)


try_count = 0
while True:
    try_count+=1
    guess_int  = int(input("Угадайте число "))
    if secret_int == guess_int:
        print(f"Угадал c {try_count} попытки!!!")
        break
    elif secret_int > guess_int:
        print("Нет, больше")
    elif secret_int < guess_int:
        print("Нет, меньше")



print("Задание №4 - Расписание занятий")
weekDays = {
    "Понедельник":  ["Алхимия","Математика","Физика","Математика"],
    "Вторник":  ["Химия","История","Физра","Литература"],
    "Среда":  ["Плавание","Программирование","Проектирование","Рисование"],
    "Четверг":  ["Чтение","Каллиграфия","Автодело","Медитация"],
    "Пятница":  ["Скорочтение","Английский","Китайский"],
    "Суббота":  [],
    "Воскресенье":  []
    }

timeOflessons = ["8.00 - 10.15","10.20 - 11.25","11.30 - 12.25","13.00 - 14.00"]


for key in weekDays:
    
    if len(weekDays[key]) == 0:
        print(f"{key} - Выходной")
    else:
        print(f"{key}:")
        for i in range(len(weekDays[key])):
            lesson = f"{i+1} - {weekDays[key][i]}: {timeOflessons[i]}"
            print(lesson)

    print("----------------------------------")


