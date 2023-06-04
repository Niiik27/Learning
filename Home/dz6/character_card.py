
reg = False
reg_gender = False
reg_race = False
reg_submit = False
gender = ""
race = ""
role = ""
name = ""
while reg ==False:

 #На первом этапе некуда возвращаться и нет смысла в сбросе заполнения
    if reg_gender == False:
        genderList = ["Мужской", "Женский"]
        textGender = ""
        for i in range(0, len(genderList)):
            textGender += f"{i} - {genderList[i]}\n"
        
        while reg_gender == False:
            myGender = int(input(f"Выберете пол:\n{textGender}> "))
            if myGender >= len(genderList) or myGender < 0:
                print("Ошибка: выбери пол из перечисленного! ")
            else:
                for i in range(0, len(genderList)):
                    if myGender == i:
                        gender = genderList[i]
                        reg_gender = True
                        print(f"Выбран {gender} пол")
                        break
#На втором этапе возврат и сброс - одно и то же. Нужно ли тут делать сброс? 
    if reg_race == False:
        raceList = ["Человек", "Эльф", "Гном", "Орк", "Троль", "Бабайка"]
        textRace = ""
        for i in range(0, len(raceList)):
            textRace += f"{i} - {raceList[i]}\n"
        textRace += f"{len(raceList)} - Назад\n"   
        # textRace += f"{len(raceList)+1} - сброс\n"  
    
        myRace = 0
        while reg_race == False:
            myRace = int(input(f"Выберете рассу:\n{textRace}> "))
            if myRace > len(raceList) or myRace < 0:
                print("Ошибка: выбери рассу из перечисленного! ")
            elif myRace == len(raceList):
                reg_race = False
                reg_gender = False
                break
            else:
                for i in range(0, len(raceList)):
                    if myRace == i:
                        race = raceList[i]
                        reg_race = True
                        print(f"Выбран {race}")
                        break
          
    if reg_race:
        role_lists = [
                        ["Воин", "Лучник", "Жрец", "Маг"],
                        ["Воин", "Лучник", "Темный колдун", "Паладин"],
                        ["Лесник", "Болотник", "Волшебник", "Пастух"],
                        ["Воин", "Наездник", "Генерал", "Призрак"],
                        ["Пакосник", "Весельчак", "Злодей", "Принцесса"],
                    ]
        default_role = ["Воин", "Лучник", "Босс", "Маг"]
        #Допустим появился новый персонаж, а его роли толком не определены, для того что бы его можно было 
        #Дальше разрабатывать ему присваиваются условные роли по умолчанию

        #И далее нам однозначно потребуется сброс заполнения карточки персонажа
        if myRace>=len(role_lists):
            roleList = default_role
        else:
            roleList = role_lists[myRace]
        textRole = ""
        for i in range(0, len(roleList)):
            textRole += f"{i} - {roleList[i]}\n"
        textRole += f"{len(roleList)} - Назад\n"   
        textRole += f"{len(roleList)+1} - Сброс\n" 
        reg_role = False
        myRole = 0
        while reg_role == False:
            myRole = int(input(f"Выберете роль:\n{textRole}> "))
            if myRole > len(roleList)+1 or myRole < 0:
                print("Ошибка: выбери роль из перечисленного! ")
            elif myRole == len(roleList):
                # reg_role = False
                reg_race = False
                break
            elif myRole > len(roleList):#Возможно нужно myRole == len(roleList+1) но так тоже сработае и меньше арифметических операций
                # reg_role = False
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
            if reg_role != False:
                reg = True
                break

    
    if len(gender) != 0 and len(race) != 0 and len(role) != 0:
        if len(name) == 0:
            name = input("Введите имя вашего персонажа или 0 что бы вернуться> ")
        else:
            rename = input("Хотите изменить имя вашего персонажа? \nEnter-нет\n1-да\n> ")
            if rename == "1":
                name = input("Введите имя вашего персонажа ")



        if len(name) != 0 and name != "0":
            submitList = ["Да", "Нет"]
            textSubmit = ""
            for i in range(0, len(submitList)):
                textSubmit += f"{i} - {submitList[i]}\n"

            while reg_submit == False:
                submit = int(input(f"Свойства персонажа заполнены. Создать персонажа?\n{textSubmit}> "))

                
                if submit >= len(submitList) or submit < 0:
                    print("Ошибка: выбери подтверждение из перечисленного! ")
                elif submit == 0:
                    print("\nИнформация о персонаже:\n"
                        f"пол персонажа {gender}\n"
                        f"Раса персонажа {race}\n"
                        f"Класс: {role}\n"
                        f"Имя: {name}\n")
                    reg = True
                    reg_submit=True
                else:
                    reg_gender = False
                    reg_race = False
                    reg_role = False
                    gender = ""
                    race = ""
                    role = ""
                    reg = False
                    break
        else:
            reg = False
            if len(gender) == 0:
                reg_gender = False
            if len(race) == 0:
                reg_gender = False  # По скольку циклы вложенные, то чтобы заново сработал нужный, нужно попасть в родительский
                # А внутри родительского защититься от повторных вводов
                reg_race = False
                # reg_role = False
                # role=""#Необходимо переопределить роль заново выбранной рассы
            if len(role) == 0:
                reg_gender = False
                reg_race = False
                reg_role = False
            if len(name) == 0:
                reg_gender = False
                reg_race = False
                reg_role = False
                gender = ""
                race = ""
                role = ""
                print("Персонаж без имени подлежит забвению. Создайте нового персонажа")
            elif name == "0":
                # reg_gender = False
                # reg_race = False
                reg_role = False
                # race = ""
                role = ""
                name = ""