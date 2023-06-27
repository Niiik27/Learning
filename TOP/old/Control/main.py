# что бы проверить код - нужно сначала пройтись по проверенным задачам - это очень не удобно,
# Приходится лишнее комментировать, или использовать exit и копировать нужный код в начало файла
# Очень нужен goto. Его не обнаружил, по этому решил для разлеления задач использовать elif
current_task = 5

if current_task == 1:
    print("Задание №1 - Карточка пользователя:")


    from datetime import date
    # Нужно было как то определить теущую дату. Немного покопавшись нашел такое решение
    current_date = date.today().timetuple()
    current_year = current_date.tm_year
    current_month = current_date.tm_mon
    current_day = current_date.tm_mday


    print(current_year,current_month,current_day)

    user_name = input("Введите Имя ")
    user_surname = input("Введите Фамилию ")
    user_birth = input("Введите дату рождения в формате ДД.ММ.ГГГГ ")
    # Здесь старый добрый сплит, есть наверное во всех языках - создает массив строк разбивая строку по выбранному символу
    birth_date = user_birth.split(".")
    birth_year = int(birth_date[2])
    birth_month = int(birth_date[1])
    birth_day = int(birth_date[0])



    user_age = current_year - birth_year - (current_month < birth_month)#Будет 0 если 
    # Если др еще не наступил то нужно уменьшить возраст на 1. Это реализовал в уравнении
    # теперь осталость проверить дни рождения в случае равенства месяцев

    if current_month == birth_month and birth_day > current_day: current_year -=1
    print(user_age)
    # Получилось не очень красиво - условие с месяцами - можно без проблем записать в формулу, а с днями призодится писать if
    # Решил погуглить - как можно было бы сделать единообразно
    # Нашел очень крутое и красивое решение требующее изучения. по этому оставлю его в коде,
    # А свое решение оставил лишь для вывода через принт

    user_age = current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day))
    print(user_age)

    userCard = {
                "user_name":user_name,
                "user_surname":user_surname,
                "user_age":user_age,
                "user_birth": user_birth,         
                }
    print(f"Имя пользователя: {userCard['user_name']}\nФамилия пользователя: {userCard['user_surname']}\nВозраст пользователя: {userCard['user_age']} лет\nДень рождения пользователя: {userCard['user_birth']} г.\n")
    print("--------------------------------------------------------")


elif current_task == 2:

    print("Задание №2 - Выбрать загадку:")

    # Это новое решение построеное на паре ответ - загадка
    riddles = {
        "лампочка": "Висит груша нельзя скушать? ",
        "ножницы": "Два кольца два конца, по середине гвоздик? ",
        "тень": "Что больше слона, и ничего не весит? "
    }

    # riddles.items - это массивчики, содержащие ключ[0],значение[1]
    # В старом решении обошлось без него
    str_riddles = ""
    

    riddle_list =list(riddles.items())
    for i in range(len(riddle_list)):# При обходе словаря в цикле в key возвращается значение ключа
        str_riddles += f"{i+1} - {riddle_list[i][1]}\n"
    way = int(input(f"Выберите загадку:\n{str_riddles}"))-1
    right_answer = riddle_list[way][0]

    # Ограничивать попытки нужно чтоб можно было корректно выйти

    try_count = 3
    win = False
    while try_count>0:
        response = input(f"Ответ на загадку (у вас {try_count} попытки): ")
        try_count-=1
        if response == right_answer:
            print("Верно!")
            win = True
            break
        else:
            print(f"Попробуйте еще раз, осталось {try_count} попытки")

    if win:
        print("Поздравляем!")
    else:
        print("Вы проиграли")

elif current_task == 3:
    import random
    print("Задание №3 - Угадай число")
    start = 1
    end = 10
    secret_int = random.randint(start,end)#Задаем любой диапазон


    try_count = 0
    while True:
        try_count+=1
        guess_int  = int(input(f"Угадайте загаданное число от {start} до {end}> "))
        if secret_int == guess_int:
            print(f"Угадал c {try_count} попытки!!!")
            break
        elif secret_int > guess_int:
            print("Нет, больше")
        elif secret_int < guess_int:
            print("Нет, меньше")

elif current_task == 4:

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

elif current_task == 5:
    # Получился длинный код, скучей условий принтами и инпутами в которых прописано зачем они нужны
    # По этому вряд ли потребуется много коментариев
    print("Задание №5 - Добавление и проверка плоьзователей")
    registeredUsers = []
    # Нужна карточка пользователя
    fields = {
                "myName":"Имя",
                "mySurName":"Фамилия",
                "myLogin":"Логин",
                "myPass": "Пароль",  
                }


    while True:# Пока очевидно что нужен цикл для множественного добавления,
        #но при услловии выхода возможно потребуются дополнительные действия,
        # а значит недостаточно указать условие выхода в объявлении цикла. по
        # этому пока просто бесконечный цикл
        
        myName = input("Введите Имя ")
        mySurName = input("Введите Фамилию ")
        
        while True:
            myLogin = input("Введите Логин ")
            # сразу же проверяем логин на уникальность
            # Если логин не уникален то придется вводит его заного
            validLogin = True
            for user in registeredUsers:
                if myLogin == user["myLogin"]:
                    # myLogin = input("Такой логин уже занят. Введите другой логин> ")
                    print("Такой логин уже занят!")
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

    finish = False
    while finish == False:
        myLogin = input("Введите Логин ")
        myPass = input("Введите пароль ")
       
        #Здесь видимо не стоит облегчать задачу по подбору пароля, а значит не нужно  сообщать что именно не правильно - логин или пароль
        # Но начать нужно с логина, потому что без логина пароля не существует
       
        match_user = False
        for i in range(len(registeredUsers)):
            user = registeredUsers[i]
            if myLogin == user["myLogin"]:# только попав сюда - можно считать что логин существует
                match_user = True
            
                if myPass == registeredUsers[i]["myPass"]:
                    
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
                        finish = True
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
                        print("")
                        userCard_str = ""
                        for key in user:
                            userCard_str+=f"{fields[key]}: {user[key]}\n"
                        print(f"Новые данные пользователя:\n{userCard_str}")
                        confirm = input("Прекратить?\nEnter - ДА\nЛюбой символ - НЕТ\n> ")
                        if confirm == "":
                            print (registeredUsers)
                            finish = True
                    break
                else:
                    match_user = False
      
        if match_user == False:
            print("Ошибка! - Неверный логин или пароль")
            # break
       
            


exit(0)

print("Задание №2 - Выбрать загадку:")

# Нужно было решить что лучше подойдет для хранения загадок. От списка отказался потому что выбирать пришлось бы через индексы,
# Изменение порядка загадок изменило бы привычные ключи выбора
# Объектом можно назначить любые ключи, можно замаскировать их под индексы, и позже переименовать в более осмысленные
# по этому пока ключи будут 1,2,3,
# Это старое решение
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


