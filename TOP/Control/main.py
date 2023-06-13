registeredUsers = []
fields = {
            "myName":"Имя",
            "mySurName":"Фамилия",
            "myLogin":"Логин",
            "myPass": "Пароль",  
            }


while True:
    
    myName = input("Введите Имя ")
    mySurName = input("Введите Фамилию ")
    myLogin = input("Введите Логин ")
    
    while True:
        validLogin = True
        for user in registeredUsers:
            if myLogin == user["myLogin"]:
                myLogin = input("Такой логин уже занят. Введите другой логин ")
                validLogin = False
                break
        if validLogin == True: break

    myPass = input("Введите пароль ")

    userCard = {
                "myName":myName,
                "mySurName":mySurName,
                "myLogin":myLogin,
                "myPass": myPass,         
                }
    print("")
    userCard_str = ""
    for key in userCard:
        userCard_str+=f"{fields[key]}: {userCard[key]}\n"
    print(f"Данные пользователя:\n{userCard_str}")
    submit = input("Enter - Подтвердить ")
    print("")
    if len(submit) == 0: 
        registeredUsers.append(userCard)
        print("Пользователь добавлен")
    else:
        print("Пользователь не добавлен")
    if len(registeredUsers)>0:
        print("")
        stopAddUsers = input("Прекратить добавление пользователей? Enter - ДА, Любой символ - НЕТ ")
        if len(stopAddUsers) == 0:
            break
print("")   
print("Теперь вы должны войти")
print("")

    
while True:
    myLogin = input("Введите Логин ")
    myPass = input("Введите пароль ")
    #Здесь видимо не стоит облегчать задачу по подбору пароля, а значит не нужно  сообщать что именно не правильно - логин или пароль
    # Но начать нужно с логина, потому что без логина пароля не существует
    validLogin = False
    for user in registeredUsers:
        if myLogin == user["myLogin"]:
            validLogin = True
            break
    if validLogin == False:
        print("Ошибка! - Неверный логин или пароль")
    else:
        validPass = False
        for user in registeredUsers:
            if myPass == user["myPass"]:
                validPass = True
                break
        if validPass == False:
            print("Ошибка! - Неверный логин или пароль")
        else:
            #Тут бы сразу после входа видеть инфо, что бы принять решение - выйти, или редактировать
            print("")
        
            userCard_str = ""
            for key in user:
                userCard_str+=f"{fields[key]}: {user[key]}\n"
            print(f"Ваши данные:\n{userCard_str}")
            menuList = ["Редактировать", "Выход"] 
            menu_txt = ""
            for i in range(len(menuList)):
                menu_txt+=f"{i+1} - {menuList[i]}\n"
            choice = input(f"Выберите действие:\n{menu_txt}")
            if choice == "2":
                break
            elif choice == "1":
                print("")
                menuList = ["Изменить имя", "Изменить фамилию","Изменить логин", "Изменить пароль"]
                menu_txt = ""
                for i in range(len(menuList)):
                    menu_txt+=f"{i+1} - {menuList[i]}\n"
                choice = input(f"Выберите действие:\n{menu_txt}")
                if choice == "1":
                    user["myName"] = input("Введите новое имя ")
                elif choice == "2":
                    user["mySurName"] = input("Введите новую фамилию ")
                elif choice == "3":
                    myLogin = input("Введите новый логин ")
                    while True:
                        validLogin = True
                        for user in registeredUsers:
                            if myLogin == user["myLogin"]:
                                myLogin = input("Такой логин уже занят. Введите другой логин ")
                                validLogin = False
                                break
                        if validLogin == True:
                            user["myLogin"] = myLogin
                            break
                elif choice == "4":
                    user["myPass"] = input("Введите новый пароль ")

                print(registeredUsers)







    

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


