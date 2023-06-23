
menuList = ["Изменить имя", "Изменить фамилию","Изменить логин", "Изменить пароль"]
def show_menu(menu_list:list):
    menu_txt = ""
    for i in range(len(menu_list)):
        menu_txt+=f"{i+1} - {menu_list[i]}\n"
    choice = input(f"Выберите действие:\n{menu_txt}> ")
    while True:
        if not choice.isdigit():
            print(f"Допустим тольлько числовой ввод!")
            choice = input(f"Выберите действие:\n{menu_txt}> ")
        elif 1<=int(choice)<=len(menu_list):
            return int(choice)
        else:
            print(f"Число должно быть в диапазоне от 1 до {len(menu_list)}!")
            choice = input(f"Выберите действие:\n{menu_txt}> ")

print(show_menu(menuList))





def menu(massiv):
    print(massiv)

def newMenu(massiv):
    for i in range(0,len(massiv)):
        print(massiv[i]["name"])

def x(massiv):
    listMenu = [
        {
            "nameFunc" : "Регистрация нового пользователья",
            "startFunc" : menu
        },
        {
            "nameFunc" : "Вход в ЛК",
            "startFunc" : newMenu
        }
    ]
    text = ""
    for i in range(0,len(listMenu)):
        text += f'{i} - {listMenu[i]["nameFunc"]}\n'
    print(text)
    m = int(input("Введите"))    
    for i in range(0,len(listMenu)):
        if m == i:
            listMenu[i]["startFunc"](massiv)
    x(massiv)


arrMass= [
    {
        "name" : "Макс"
    },
    {
        "name" : "Денис"
    },
]

x(arrMass)

usersList = [] # Список пользовательей

while True:
    x = int(input("Введите:\n1-Регистрация нового пользователья\n2-Вход в личный кабинет"))
    if x == 1: # цикл для регистрации новго пользователя
        print("---- Регистрация ----")
        while True:
            regUser = {
                "userLogin" : "",
                "userPassword" : "",
                "userName" : "",
                "userFirstName" : "",
            }
            while True:
                regLogin = input("Введите логин: ") # admin1
                if len(usersList) > 0:
                    for i in range(0,len(usersList)):
                        if regLogin != usersList[i]["userLogin"]:
                            regUser["userLogin"] = regLogin
                            
                        elif len(usersList) - 1 == i:
                            print("Данный логин уже занят\n введите другой")
                            regUser["userLogin"] = ""
                            break
                else:
                    regUser["userLogin"] = regLogin
                if len(regUser["userLogin"]) > 0:
                    break
            regUser["userPassword"] = input("Введите пароль нового пользователя: ")
            regUser["userName"] = input("Введите имя нового пользователя: ")
            regUser["userFirstName"] = input("Введите фамилию нового пользователя: ")
            print("Регистрация завершена")
            check = int(input("1 - подвтерить\n2 - ввести данные снова"))
            if check == 1:
                usersList.append(regUser)
                print(usersList)
                break
            elif check == 2:
                print("---- Регистрация ----")
    
    elif x == 2:
        print("-- Вход в ЛК")
        inLogin = input("Введите логин: ")
        inPassword = input("Введите пароль: ")
        for i in range(0,len(usersList)):
            if inLogin == usersList[i]["userLogin"] and inPassword == usersList[i]["userPassword"]:
                print("Вход выполнен")
                while True:
                    infoUser = int(input("1-Посмотр инфо\n2-Ред инфо\n3-Выход"))
                    if infoUser == 1:
                        print(f'Имя : {usersList[i]["userName"]}')
                        print(f'Фамилия : {usersList[i]["userFirstName"]}')
                        print(f'Логин : {usersList[i]["userLogin"]}')
                        print(f'Пароль : {usersList[i]["userPassword"]})')
                    elif infoUser == 2:
                        print("Редактирование данных")
                        upDate = int(input("1-Имя\n2-Фамилия\n3-Пароль"))
                        if upDate == 1:
                            print(f'ваше имя {usersList[i]["userName"]}')
                            usersList[i]["userName"] = input("новое имя: ")
                        elif upDate == 2:
                            print(f'ваша фамилия {usersList[i]["userFirstName"]}')
                            usersList[i]["userFirstName"] = input("новое фамилия: ")
                        elif upDate == 3:
                            print(f'ваш пароль {usersList[i]["userPassword"]}')
                            usersList[i]["userPassword"] = input("новой пароль: ")
                    elif infoUser == 3:
                        break
                break
            elif len(usersList) - 1 == i:
                print("Неверный логин или пароль")





