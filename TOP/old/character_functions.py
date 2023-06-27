def regName(myName):
    print(myName)
    globalReg()

def regGender():
    listGender = ["Муж","Жен"]
    textGender = ""
    for i in range(0,len(listGender)):
        textGender += f"{i} - {listGender[i]}\n"
    myGender = int(input(f"Выберите пол:\n{textGender}> "))
    for i in range(0,len(listGender)):
        if myGender == i:
            myGender = listGender[i]
            break
    globalReg()

def regRace():
    listRace = ["Человек", "Эльф", "Гном", "Орк", "Троль", "Бабайка"]
    textRace = ""
    for i in range(0,len(listRace)):
        textRace += f"{i} - {listRace[i]}\n"
    myRace = int(input(f"Выберите рассу:\n{textRace}> "))
    for i in range(0,len(listRace)):
        if myRace == i:
            myRace = listRace[i]
            regRole(i)
            break
    
    globalReg()


def regRole(race_num):
    listRoles = [
    ["Воин", "Лучник", "Жрец", "Маг"],
    ["Воин", "Лучник", "Темный колдун", "Паладин"],
    ["Лесник", "Болотник", "Волшебник", "Пастух"],
    ["Воин", "Наездник", "Генерал", "Призрак"],
    ["Пакосник", "Весельчак", "Злодей", "Принцесса"],
        ]
    listRole = listRoles[race_num]
    textRole = ""
    for i in range(0,len(listRole)):
        textRole += f"{i} - {listRole[i]}\n"
    myRole = int(input(f"Выберите рассу:\n{textRole}> "))
    for i in range(0,len(listRole)):
        if myRole == i:
            myRole = listRole[i]
            break
    globalReg()



def regItem(item, itemList):
    textItem = ""
    for i in range(0,len(itemList)):
        textItem += f"{i} - {itemList[i]}\n"
    myItem = int(input(f"Выберите {item}:\n{textItem}> "))
    for i in range(0,len(itemList)):
        if myItem == i:
            myItem = itemList[i]
            break
    globalReg()





def globalReg():
    print("Регистрация персонажа ")
    x = int(input("Выбор действия:\n1 - Ввод имени\n2 - Ввод Гендера\n3 - Ввод Рассы\n4 - Ввод пункта пола\n5 - Ввод пункта рассы\n> "))
    if x == 1:
        regName(input("Имя: "))
    elif x == 2:
        regGender()
    elif x == 3:
        regRace()
    elif x == 4:
        regItem("Пол",["Муж","Жен"])
    elif x == 5:
        regItem("Рассу",["Человек", "Эльф", "Гном", "Орк", "Троль", "Бабайка"])

globalReg()