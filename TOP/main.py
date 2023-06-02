# genderList = ["Мужской","Женский"]
# raceList = ["Человек", "Эльф"]
# print(raceList,"Создали список")
# raceList.append("Гном")
# print(raceList,"Добавили гнома в список")
# raceList.pop(1)
# print(raceList,"Удалили эльфа из списка")
# raceList.clear()
# print(raceList,"Удалили всех")

# numberList = [3,1,3,7,9,5,4,2,8,6]
# print(numberList)
# for i in range(0,len(numberList)):
#     numberList[i]=numberList[i]**2
#     # print(numberList[i])
# print(numberList)
# numberList.sort()

# listN = [[1,2,3,4,5],
#          [6,7,8,9,10],
#          [11,12,13,14,15],
#          [16,17,18,19,20],
#          [21,22,23,24,25]]
# print(listN[1][4])

# for i in range(0,len(listN)):
#     for j in range(0,len(listN[i])):
#         print(listN[i][j])
#     print("----------------------------------------------")
reg = False
while reg ==False:

    genderList = ["Мужской","Женский","Назад"]
    textGender = ""
    for i in range(0, len(genderList)):
        textGender += f"{i} - {genderList[i]}\n"
    reg_gender = False
    while reg_gender == False:
        myGender = int(input(f"Выберете пол:\n{textGender}>"))
        if myGender >= len(genderList) or myGender < 0:
            print("Ошибка: выбери пол из перечисленного! ")
        else:
            for i in range(0, len(genderList)):
                if myGender == i:
                    gender = genderList[i]
                    reg_gender = True
                    print(f"Выбран {gender} пол")
                    break


    raceList = ["Человек", "Эльф", "Гном", "Орк","Троль"]
    textRace = ""
    for i in range(0, len(raceList)):
        textRace += f"{i} - {raceList[i]}\n"
    textRace += f"{len(raceList)} - назад\n"   
    reg_race = False
    while reg_race == False:
        myRace = int(input(f"Выберете рассу:\n{textRace}>"))
        if myRace > len(raceList) or myRace < 0:
            print("Ошибка: выбери рассу из перечисленного! ")
        elif myRace == len(raceList):
            reg_race = False
            break
        else:
            for i in range(0, len(raceList)):
                if myRace == i:
                    race = raceList[i]
                    reg_race = True
                    print(f"Выбран {race}")
                    break
        if reg_race != False:
            reg = True
            break
                    

                # print(f"я выбрал {raceList[myRace]} пк сравнивает с {raceList[i]}")


    roleList = ["Воин","Лучник","Маг"]
