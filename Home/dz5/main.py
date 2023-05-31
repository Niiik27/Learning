# -----------------------------------------------------------------------------------------------------#
# --------------Использование циклов внутри циклов, возврат значений,  условия-------------------------#
# -----------------------------------------------------------------------------------------------------#
print("Регистрация персонажа")
gender = ""
race = ""
role = ""
name = ""

# Если эти переменные указать вне цикла, то они не будут обновляться в случае возврата, и это можно использовать
# для заполнения только незаполненного поля
reg_gender = False
reg_race = False
reg_role = False

reg = False
while reg == False:
    # reg_gender = False
    while reg_gender == False:
        if len(gender) == 0:
            gender = input("Выберете пол персонажа\n1-муж\n2-жен\nEnter - пропустить\n: ")

            if gender == "1":
                gender = "Мужской"
                reg_gender = True
                print(f"Выбран {gender} пол")
            elif gender == "2":
                gender = "Женский"
                reg_gender = True
                print(f"Выбран {gender} пол")
            elif gender == "":
                reg_gender = True
                print("Пол не выбран")
            else:
                print("Ошибка! - Выберете пол из перечисленного!")
                gender = ""
        else:
            reg_gender = True

        if reg_gender == True:
            # reg_race = False
            while reg_race == False:
                if len(race) == 0:
                    race = input("Выберете рассу персонажа\n1-Человек\n2-Эльф\n0-вернуться\nEnter - пропустить\n: ")

                    if race == "1":
                        race = "Человек"
                        reg_race = True
                        print(f"Выбран {race}")
                    elif race == "2":
                        race = "Эльф"
                        reg_race = True
                        print(f"Выбран {race}")
                    elif race == "0":
                        reg_gender = False
                        gender = ""
                        race = ""
                        break
                    elif race == "":
                        reg_race = True
                        print("Расса не выбрана")
                    else:
                        print("Ошибка! - Выберете рассу из перечисленного!")
                        race = ""
                else:
                    reg_race = True
                if reg_race == True:
                    # reg_role = False
                    if race == "Человек":
                        print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
                        while reg_role == False:
                            if len(role) == 0:
                                role = input("введите 1,2,3 или 4 для выбора класса, 0-вернуться\n: ")

                                reg_role = True
                                if role == "1":
                                    role = "Воин"
                                elif role == "2":
                                    role = "Лучник"
                                elif role == "3":
                                    role = "Жрец"
                                elif role == "4":
                                    role = "Маг"
                                elif role == "0":
                                    reg_race = False
                                    reg_role = False
                                    role = ""
                                    race = ""
                                    break
                                elif role == "":
                                    pass
                                else:
                                    print("Ошибка! - Выберете класс человека из перечисленного!")
                                    reg_role = False
                                    role = ""
                            else:
                                reg_role = True
                    elif race == "Эльф":
                        print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
                              "4-Паладин\n")
                        while reg_role == False:
                            if len(role) == 0:
                                role = input("введите 1,2,3 или 4 для выбора класса, 0-вернуться\n: ")

                                reg_role = True
                                if role == "1":
                                    role = "Воин"
                                elif role == "2":
                                    role = "Лучник"
                                elif role == "3":
                                    role = "Темный Колдун"
                                elif role == "4":
                                    role = "Паладин"
                                elif role == "0":
                                    reg_race = False
                                    reg_role = False
                                    role = ""
                                    race = ""
                                    break
                                elif role == "":
                                    pass
                                else:
                                    print("Ошибка! - Выберете класс эльфа из перечисленного!")
                                    role = ""
                                    reg_role = False
                            else:
                                reg_role = True
                    elif race == "":
                        role = ""
                        reg_role = True
                        #Если расса не выбрана, то мы не знаем какая роль будет у персонажа
                        #Просто использовать соответствующие значения переменных - будет не корректно
    if len(name) == 0:
        name = input("Введите имя вашего персонажа ")
    else:
        rename = input("Хотите изменить имя вашего персонажа? \nEnter-нет\n1-да\n:")
        if len(rename)!=0:
            name = input("Введите имя вашего персонажа ")
    # Далее - если поле пустое, то нужно будет сбросить соответствующий флаг
    # Будет много if По этому частично их объеденю, и продублирую, что бы код был короче и читабельнее
    # Если все будет работать хорошо, то можно будет оптимизировать и разложить по своим if

    # print(len(gender) != 0 , len(race) != 0 ,len(role) != 0 , len(name) != 0)

    if len(gender) != 0 and len(race) != 0 and len(role) != 0 and len(name) != 0:
        print("\nИнформация о персонаже:\n"
              f"пол персонажа {gender}\n"
              f"Раса персонажа {race}\n"
              f"Класс: {role}\n"
              f"Имя: {name}\n")
        reg = True
    else:
        reg = False
        if len(gender) == 0:
            reg_gender = False
        if len(race) == 0:
            reg_gender = False#По скольку циклы вложенные, то чтобы заново сработал нужный, нужно попасть в родительский
            #А внутри родительского защититься от повторных вводов
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
            gender=""
            race=""
            role = ""
            print("Персонаж без имени подлежит забвению. Создайте нового персонажа")
