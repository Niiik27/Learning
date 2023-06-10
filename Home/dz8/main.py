import random

blackList = ["я", "коля", "денис"]
# Задолбался вводить гостей. на тестовый период будет тестовый массив
test_guestList = [
    {
        "nameGuest": "Николай",
        "ageGuest": 42,
        "genderGuest": "м",
        "id": "ID_00000",
        "numberGuest": 1,
    },
    {
        "nameGuest": "Марина Ивановна",
        "ageGuest": 66,
        "genderGuest": "ж",
        "id": "ID_00001",
        "numberGuest": 2,
    },
    {
        "nameGuest": "Саша",
        "ageGuest": 12,
        "genderGuest": "м",
        "id": "ID_00002",
        "numberGuest": 3,
    },
    {
        "nameGuest": "Оля",
        "ageGuest": 13,
        "genderGuest": "ж",
        "id": "ID_00003",
        "numberGuest": 4,
    },
    {
        "nameGuest": "Илья",
        "ageGuest": 20,
        "genderGuest": "м",
        "id": "ID_00004",
        "numberGuest": 5,
    },
    {
        "nameGuest": "Юля",
        "ageGuest": 22,
        "genderGuest": "ж",
        "id": "ID_00005",
        "numberGuest": 6,
    },
    {
        "nameGuest": "Даня",
        "ageGuest": 11,
        "genderGuest": "м",
        "id": "ID_00006",
        "numberGuest": 7,
    },
    {
        "nameGuest": "Мила",
        "ageGuest": 12,
        "genderGuest": "ж",
        "id": "ID_00007",
        "numberGuest": 8,
    },
    {
        "nameGuest": "Иван Иваныч",
        "ageGuest": 56,
        "genderGuest": "м",
        "id": "ID_00008",
        "numberGuest": 9,
    },
    {
        "nameGuest": "Елена",
        "ageGuest": 34,
        "genderGuest": "ж",
        "id": "ID_00009",
        "numberGuest": 10,
    },
    {
        "nameGuest": "Тема",
        "ageGuest": 14,
        "genderGuest": "м",
        "id": "ID_00010",
        "numberGuest": 11,
    },

]
guestList = []
guestList = test_guestList

menu_items = ["Добавить гостей", "Удалить гостя по имени", "Удалить гостя по номеру", "Удалить гостя по id",
              "Удалить гостя по индексу", "Удалить всех взрослых", "Удалить всех детей", "Удалить всех мужчин",
              "Удалить всех женщин", "Просмотр гостей", "Закончить"]
offset_menu = 1
max_limit = 11
finish_range = [6, max_limit]
# Возникла крутая идея по формированию id
idSymbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
idLen = 8
n = 0

while len(guestList) <= finish_range[1]:
    strItems = ""
    for i in range(0,
                   len(menu_items) - 1 + int(finish_range[0] < len(guestList) < finish_range[1])):  # количесто итераций
        # зависит от количества гостей. что бы не дописывать отдельно меню закончить сделал изменяемую итерацию
        strItems += f"{i + offset_menu} - {menu_items[i]}\n"
    print("--------------------------------------")
    print("Регистрация гостей: ")
    guest_action = int(input(f"Выберите действие:\n{strItems}> "))

    # elif был в прошлый раз, где то ближе к концу я понял, что тут понятней и проще будет match/case так elif
    # приходилось комментировать и следовать порядку расположения в массиве, что бы не запутаться
    match menu_items[guest_action - offset_menu]:
        case "Добавить гостей":
            while len(guestList) < finish_range[1]:

                nameGuest = input("Введите имя гостя или нажмите Enter, что бы прекратить ввод:> ")
                if len(nameGuest) == 0: break
                if nameGuest in blackList:
                    print("Этого человека приглашать нельзя!")
                    continue  # Если есть break, то должен быть и continue. И здесь было бы проще с ним
                ageGuest = int(input("Введите возраст гостя:> "))
                if ageGuest < 10:
                    print("Нельзя приглашать детей младше 10 лет! ")
                    continue
                genderGuest = input("Введите пол гостя:> ")
                # if not (genderGuest == "м" or genderGuest == "ж" or genderGuest == "m" or genderGuest == "w"):
                if genderGuest == "m":
                    genderGuest = "м"
                elif genderGuest == "w":
                    genderGuest = "ж"
                elif not (genderGuest == "ж" or genderGuest == "м"):
                    print("Этих нельзя приглашать! ")
                    continue
                numberGuest = n  # порядковый номер навсякий случай, либо для видимости для пользователя
                idGuest = ""  # id - что то уникальное для разработчика
                n += 1  # После всех проверок начинаеся код добавления, а значит n можно увеличить. Если сейчас то нумерация будет с 1 а не с 0
                while True:
                    for _ in range(idLen):  # Подсмотрел в math/case - i сейчас не нужно
                        symbolIndex = random.randint(0, len(idSymbols) - 1)
                        idGuest += idSymbols[symbolIndex]
                    # id должен быть уникальным - длина строки id повышает уникальность, но проверять все таки нужно
                    for guest in guestList:
                        if guest["id"] == idGuest:
                            idGuest = ""
                            break  # Придется выйти из цикла и войти заново, потому что новый id нужно будет сравнивать с уже проверенными
                    if len(idGuest) != 0: break  # Если id обнулился то выход из цикла не сработает

                infoGuest = {
                    "nameGuest": nameGuest,
                    "ageGuest": ageGuest,
                    "genderGuest": genderGuest,
                    "id": idGuest,
                    "numberGuest": n,
                }
                guestList.append(infoGuest)
                # Интересно посмотреть что получилось
                print("--------------------------------------")
                for guest in guestList:
                    print(f"Имя гостя - {guest['nameGuest']}")
                    print(f"Возраст гостя - {guest['ageGuest']}")
                    print(f"Пол гостя - {guest['genderGuest']}")
                    print(f"Номер гостя - {guest['numberGuest']}")
                    print(f"id - {guest['id']}")
                    print("--------------------------------------")
                nextGuest = False
                while nextGuest == False:
                    nextGuest = (len(input("Нажмите Enter что бы продолжить ввод> ")) == 0)

        case "Удалить гостя по имени":

            if len(guestList) == 0:
                print("Вы не можете удалить гостя из пустого списка")
            else:
                guestNames = "Список гостей до удаления: "
                for guest in guestList: guestNames += f"{guest['nameGuest']}, "
                print(guestNames)
                del_guest = input("Введите имя удаляемого гостя:> ")
                for guest in guestList:
                    if guest["nameGuest"] == del_guest:
                        guestList.remove(guest)
                        break
                guestNames = "Список гостей после удаления : "
                for guest in guestList: guestNames += f"{guest['nameGuest']}, "
                print(guestNames)
                nextGuest = False
                while nextGuest == False:
                    nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить гостя по номеру":
            if len(guestList) == 0:
                print("Вы не можете удалить гостя из пустого списка")
            else:
                guestNumbers = "Список гостей до удаления:\n"
                for guest in guestList: guestNumbers += f"{guest['numberGuest']} - {guest['nameGuest']}\n"
                print(guestNumbers)
                del_guest = int(input("Введите номер удаляемого гостя:> "))
                for guest in guestList:
                    if guest["numberGuest"] == del_guest:
                        guestList.remove(guest)
                        break
                guestNumbers = "Список гостей после удаления:\n"
                for guest in guestList: guestNumbers += f"{guest['numberGuest']} - {guest['nameGuest']}\n"
                print(guestNumbers)
                nextGuest = False
                while nextGuest == False:
                    nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить гостя по id":
            if len(guestList) == 0:
                print("Вы не можете удалить гостя из пустого списка")
            else:
                guestNumbers = "Список гостей до удаления:\n"
                for guest in guestList: guestNumbers += f"{guest['nameGuest']} - {guest['id']}\n"
                print(guestNumbers)
                del_guest = input("Введите id удаляемого гостя:> ")
                for guest in guestList:
                    if guest["id"] == del_guest:
                        guestList.remove(guest)
                        break
                guestNumbers = "Список гостей после удаления:\n"
                for guest in guestList: guestNumbers += f"{guest['nameGuest']} - {guest['id']}\n"
                print(guestNumbers)
                nextGuest = False
                while nextGuest == False:
                    nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить гостя по индексу":
            if len(guestList) == 0:
                print("Вы не можете удалить гостя из пустого списка")
            else:
                guestNames = "Список гостей до удаления: "
                for guest in guestList: guestNames += f"{guest['nameGuest']}, "
                print(guestNames)
                del_guest = int(input("Введите индекс удаляемого гостя:> "))
                if 0 <= del_guest < len(guestList):
                    guestList.pop(del_guest)
                else:
                    print("Нет гостей с таким индексом!")
                guestNames = "Список гостей после удаления: "
                for guest in guestList: guestNames += f"{guest['nameGuest']}, "
                print(guestNames)
                nextGuest = False
                while nextGuest == False:
                    nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить всех взрослых":
            guestNames = "Список гостей до удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['ageGuest']}\n"
            print(guestNames)
            # Здесь будет сложнее так как придется столкнуться с изменением размера массива во время итерации
            # Потребуется цикл для поиска нужного элемента и цикл для повторного вхождения в поиск for - ищет,
            # while запускает повторный поиск. если нет удаляемого гостя то повторного поиска не будет

            start = 0
            while True:
                del_guest = False
                for i in range(start, len(guestList)):
                    guest = guestList[i]
                    if guest["ageGuest"] > 17:
                        guestList.pop(i)
                        # или guestList.remove(guest)
                        del_guest = True
                        start = i
                        break
                if del_guest == False: break
            guestNames = "Список гостей после удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['ageGuest']}\n"
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить всех детей":  # Далее все тоже самое по этому без комментариев
            guestNames = "Список гостей до удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['ageGuest']}\n"
            print(guestNames)
            start = 0
            while True:
                del_guest = False
                for i in range(start, len(guestList)):
                    guest = guestList[i]
                    if guest["ageGuest"] < 18:
                        guestList.remove(guest)
                        # или guestList.pop(i)
                        del_guest = True
                        start = i
                        break
                if del_guest == False: break
            guestNames = "Список гостей после удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['ageGuest']}\n"
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить всех мужчин":  # Далее все тоже самое по этому без комментариев
            guestNames = "Список гостей до удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['genderGuest']}\n"
            print(guestNames)
            start = 0
            while True:
                del_guest = False
                for i in range(start, len(guestList)):
                    guest = guestList[i]
                    if guest["genderGuest"] == "м":
                        guestList.remove(guest)
                        del_guest = True
                        start = i
                        break
                if del_guest == False: break
            guestNames = "Список гостей после удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['genderGuest']}\n"
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Удалить всех женщин":  # Далее все тоже самое по этому без комментариев
            guestNames = "Список гостей до удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['genderGuest']}\n"
            print(guestNames)
            start = 0

            while True:
                del_guest = False
                for i in range(start, len(guestList)):
                    guest = guestList[i]
                    if guest["genderGuest"] == "ж":
                        guestList.remove(guest)
                        del_guest = True
                        start = i
                        break
                if del_guest == False: break
            guestNames = "Список гостей после удаления:\n"
            for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['genderGuest']}\n"
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

        case "Просмотр гостей":
            for guest in guestList:
                print("--------------------------------------")
                print(f"Имя гостя - {guest['nameGuest']}")
                print(f"Возраст гостя - {guest['ageGuest']}")
                print(f"Пол гостя - {guest['genderGuest']}")
                print(f"Номер гостя - {guest['numberGuest']}")
                print(f"id - {guest['id']}")
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Посмотрели? Нажмите Enter> ")) == 0)

        case "Закончить":
            if finish_range[0] < len(guestList) < finish_range[1]:
                offer = input("Прекратить регистрацию?> ")
                if offer == "y" or offer == "yes" or offer == "д" or offer == "да":
                    for guest in guestList:
                        print("--------------------------------------")
                        print(f"Имя гостя - {guest['nameGuest']}")
                        print(f"Возраст гостя - {guest['ageGuest']}")
                        print(f"Пол гостя - {guest['genderGuest']}")
                        print(f"Номер гостя - {guest['numberGuest']}")
                        print(f"id - {guest['id']}")
                    break
