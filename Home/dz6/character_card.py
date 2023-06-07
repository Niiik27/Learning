
reg = False
reg_gender = False
reg_race = False
reg_role = False
reg_submit = False
gender = ""
race = ""
role = ""
name = ""
myRole = 0
genderList = ["Мужской", "Женский"]
raceList = ["Человек", "Эльф", "Гном", "Орк", "Троль", "Бабайка"]
role_lists = [
    ["Воин", "Лучник", "Жрец", "Маг"],
    ["Воин", "Лучник", "Темный колдун", "Паладин"],
    ["Лесник", "Болотник", "Волшебник", "Пастух"],
    ["Воин", "Наездник", "Генерал", "Призрак"],
    ["Пакосник", "Весельчак", "Злодей", "Принцесса"],
]
roleList = []
default_role = ["Роль 1", "Роль 2", "Роль 3", "Роль 4"]
textRole = ""
submitList = ["Да", "Нет"]

"""
Для оптимизации эти переменные создал вне цикла.
Код немного упростил - теперь нельзя пропускать выбор
"""

textGender = ""
for i in range(0, len(genderList)):
    textGender += f"{i} - {genderList[i]}\n"

textRace = ""
for i in range(0, len(raceList)):
    textRace += f"{i} - {raceList[i]}\n"
textRace += f"{len(raceList)} - Назад\n"

textSubmit = ""
for i in range(0, len(submitList)):
    textSubmit += f"{i} - {submitList[i]}\n"

while reg == False:
    while reg_gender == False:
        myGender_str = input(f"Выберете пол:\n{textGender}> ")
        if len(myGender_str) == 0:
            reg_gender = True
        else:
            myGender = int(myGender_str)
            if myGender >= len(genderList) or myGender < 0:
                print("Ошибка: выбери пол из перечисленного! ")
            else:
                for i in range(0, len(genderList)):
                    if myGender == i:
                        gender = genderList[i]
                        print(f"Выбран {gender} пол")
                        reg_gender = True
                        break

    while reg_race == False:
        myRace_str = input(f"Выберете рассу:\n{textRace}> ")
        if len(myRace_str) == 0:
            reg_race = True
        else:
            myRace = int(myRace_str)
            if myRace > len(raceList) or myRace < 0:
                print("Ошибка: выбери рассу из перечисленного! ")
            elif myRace == len(raceList):
                reg_race = False
                reg_gender = False
                break
            else:
                for i in range(0, len(raceList)):
                    if myRace == i:
                        reg_race = True
                        print(f"Выбран {race}")
                        race = raceList[i]
                        if myRace>=len(role_lists):
                            roleList = default_role
                        else:
                            roleList = role_lists[myRace]
                        textRole = ""
                        for i in range(0, len(roleList)):
                            textRole += f"{i} - {roleList[i]}\n"
                        textRole += f"{len(roleList)} - Назад\n"
                        textRole += f"{len(roleList)+1} - Сброс\n"


    while reg_role == False:
        myRole_str = input(f"Выберете роль:\n{textRole}> ")
        if len(myRole_str) == 0:
            reg_role = True
        else:
            myRole = int(myRole_str)
            if myRole > len(roleList)+1 or myRole < 0:
                print("Ошибка: выбери роль из перечисленного! ")
            elif myRole == len(roleList):
                reg_race = False
                break
            elif myRole > len(roleList):
                reg_race = False
                reg_gender = False
                break
            else:
                for i in range(0, len(roleList)):
                    if myRole == i:
                        role = roleList[i]
                        reg_role = True
                        print(f"Выбран {role}")
                        break


    if len(name) == 0:
        name = input("Введите имя вашего персонажа или 0 чтобы вернуться> ")
    else:
        print(f"Вашего персонажа зовут {name}")
        rename = input("Хотите изменить имя вашего персонажа? \nEnter-нет\n1-да\n> ")
        if rename == "1":
            name = input("Введите имя вашего персонажа ")
git

    if len(gender) != 0 and len(race) != 0 and len(role) != 0 and len(name) != 0 and name != "0":
        while reg_submit == False:
            submit_str = input(f"Свойства персонажа заполнены. Создать персонажа?\n{textSubmit}> ")

            if len(submit_str) == 0:
                submit = 0
            else:
                submit = int(submit_str)
            if submit >= len(submitList) or submit < 0:
                print("Ошибка: выбери подтверждение из перечисленного! ")
            elif submit == 0:
                print(f"\nИнформация о персонаже:\nПол: {gender}\nРасса: {race}\nКласс: {role}\nИмя: {name}\n")
                reg = True
                reg_submit=True
            elif submit == 1:#Можно было и помягче отреагировать, но как то нужно увидеть что все работает
                reg_gender = False
                reg_race = False
                reg_role = False
                gender = ""
                race = ""
                role = ""
                name = ""
                print("Создание текущего персонажа отменено. Создайте персонажа заново")
                break
    elif len(name) == 0:
        reg_gender = False
        reg_race = False
        reg_role = False
        gender = ""
        race = ""
        role = ""
        print("Персонаж без имени подлежит забвению. Создайте нового персонажа")
    elif name == "0":
        reg_role = False
        role = ""
        name = ""
    elif len(gender) == 0:
        reg_gender = False
    elif len(race) == 0:
        reg_race = False
    elif len(role) == 0:
        reg_role = False

