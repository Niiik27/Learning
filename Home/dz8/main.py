import random


# Задолбался вводить гостей. на тестовый период будет тестовый массив
# Можно пользоваться этим, можно добавлять еще, можно отключить
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
blackList = ["я", "коля", "денис"]
guestList = []
# просто переопределил, чтоб изменение кода можно было решить только за счет коментария
guestList = test_guestList

menu_items = ["Добавить гостей", "Удалить гостя по имени", "Удалить гостя по номеру", "Удалить гостя по id",
              "Удалить гостя по индексу", "Удалить гостя по возрасту", "Удалить всех взрослых", "Удалить всех детей", "Удалить всех мужчин",
              "Удалить всех женщин", "Просмотр гостей", "Закончить"]
offset_menu = 1
max_limit = 10
finish_range = [5, max_limit]
# Возникла идея по формированию id
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
    # Сначала делал elif по индексу - стало неудобно, потому что новое добавление пункта в меню приводило к изменению elif
    # по этому перешел на match/case стало на много удобней и понятней, но возникли сомнения в работоспособности на python <3.10
    # затем нашел альтернативу match/case - index. так тоже удобно и читабельно и можно будет не соблюдать порядок, если меню изменится
    # Теперь match/case - дополнительный вариант - там есть старые комментарии, но новые туда не переносил
    # по сути там тоже самое, и можно не смотреть. а удалять жалко
    if guest_action - offset_menu == menu_items.index("Добавить гостей"):
        while len(guestList) < finish_range[1]:
            # теперь ввод данных - это режим. сначала нужно его включить, потом заполнять список гостей
            # получаются длинные колонки текста, по этому все этапы тормозятся инпутом, что бы можно было
            # увидеть результат преред продолжением
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
            # храниться должно в едином формате. далее сохраненные данные будут прроверяться только в кириллице
            if genderGuest == "m":
                genderGuest = "м"
            elif genderGuest == "w":
                genderGuest = "ж"
            elif not (genderGuest == "ж" or genderGuest == "м"):
                print("Этих нельзя приглашать! ")
                continue
            numberGuest = n  # порядковый номер навсякий случай, либо для видимости пользователю.
            # Он соответствует порядку добавления, и не меняется после удаления предыдущих гостей
            idGuest = ""  # id - что то уникальное, нужно для использования в коде, и может быть скрытым от пользователя
            n += 1  # После всех проверок начинаеся код добавления, а значит n можно увеличить до этого, что бы нумерация гостей шла с 1
            # Здесь строится уникальный id
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
            # когда есть все данные - записываем их в словарь - описание гостя
            infoGuest = {
                "nameGuest": nameGuest,
                "ageGuest": ageGuest,
                "genderGuest": genderGuest,
                "id": idGuest,
                "numberGuest": n,
            }
            #а словарь сохраняем в список гостей
            guestList.append(infoGuest)
            # Интересно посмотреть что получилось - сразу весь список
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

    elif guest_action - offset_menu == menu_items.index("Удалить гостя по имени"):

        if len(guestList) == 0:
            nextGuest = False
            # print заменил на input что бы можно было прочитать надпись, откликнуться, и дать коду работать дальше
            # Этот прием использовал дальше довольно часто, он узнаваем, по этому далее не буду его комментировать
            while nextGuest == False:
                nextGuest = (len(input("Нелзя удалить гостя из пустого списка! Нажмите Enter что бы продолжить> ")) == 0)
        else:
            # при удалении показывается до и после. в сокращенном виде, что бы было легче понять как все прошло
            guestNames = "Список гостей до удаления: "
            for guest in guestList: guestNames += f"{guest['nameGuest']}, "#Удобнее видеть строку
            print(guestNames)
            del_guest = input("Введите имя удаляемого гостя:> ")
            for guest in guestList:
                if guest["nameGuest"] == del_guest:
                    guestList.remove(guest)# использовал for без i по этому удаляю по объекту, но может и с i удалял бы так же - все равно
                    break
            guestNames = "Список гостей после удаления : "
            for guest in guestList: guestNames += f"{guest['nameGuest']}, "
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

    elif guest_action - offset_menu == menu_items.index("Удалить гостя по возрасту"):

        if len(guestList) == 0:
            nextGuest = False
            # print заменил на input что бы можно было прочитать надпись, откликнуться, и дать коду работать дальше
            # Этот прием использовал дальше довольно часто, он узнаваем, по этому далее не буду его комментировать
            while nextGuest == False:
                nextGuest = (len(input("Нелзя удалить гостя из пустого списка! Нажмите Enter что бы продолжить> ")) == 0)
        else:
            # при удалении показывается до и после. в сокращенном виде, что бы было легче понять как все прошло
            guestNames = "Список гостей до удаления: "
            for guest in guestList: guestNames += f"{guest['nameGuest']}, "#Удобнее видеть строку
            print(guestNames)
            del_guest = int(input("Введите возраст удаляемого гостя:> "))
            for guest in guestList:
                if guest["ageGuest"] == del_guest:
                    guestList.remove(guest)# использовал for без i по этому удаляю по объекту, но может и с i удалял бы так же - все равно
                    break
            guestNames = "Список гостей после удаления : "
            for guest in guestList: guestNames += f"{guest['nameGuest']}, "
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

    elif guest_action - offset_menu == menu_items.index("Удалить гостя по номеру"):
        if len(guestList) == 0:
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нелзя удалить гостя из пустого списка! Нажмите Enter что бы продолжить> ")) == 0)
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

    elif guest_action - offset_menu == menu_items.index("Удалить гостя по id"):
        if len(guestList) == 0:
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нелзя удалить гостя из пустого списка! Нажмите Enter что бы продолжить> ")) == 0)
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

    elif guest_action - offset_menu == menu_items.index("Удалить гостя по индексу"):
        if len(guestList) == 0:
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нелзя удалить гостя из пустого списка! Нажмите Enter что бы продолжить> ")) == 0)
        else:
            guestNames = "Список гостей до удаления:\n"
            for i in range(len(guestList)):
                guest = guestList[i]
                guestNames += f"{i} - {guest['nameGuest']},\n"
            print(guestNames)
            del_guest = int(input("Введите индекс удаляемого гостя:> "))
            if 0 <= del_guest < len(guestList):
                guestList.pop(del_guest)
            else:
                print("Нет гостей с таким индексом!")
            guestNames = "Список гостей после удаления:\n"
            for i in range(len(guestList)):
                guest = guestList[i]
                guestNames += f"{i} - {guest['nameGuest']},\n"
            print(guestNames)
            nextGuest = False
            while nextGuest == False:
                nextGuest = (len(input("Нажмите Enter что бы продолжить> ")) == 0)

    elif guest_action - offset_menu == menu_items.index("Удалить всех взрослых"):
        guestNames = "Список гостей до удаления:\n"
        for guest in guestList: guestNames += f"{guest['nameGuest']} - {guest['ageGuest']}\n"
        print(guestNames)
        # Здесь будет сложнее так как придется столкнуться с изменением размера массива во время итерации
        # Потребуется цикл для поиска нужного элемента и цикл для повторного вхождения в поиск for - ищет,
        # while запускает повторный поиск. если нет удаляемого гостя то повторного поиска не будет
        # Еще была идея - создать список удаляемых элементов, из него сделать цикл, а основной список был бы жертвой
        # Просто но не интересно
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

    elif guest_action - offset_menu == menu_items.index("Удалить всех детей"):  # Далее все тоже самое по этому без комментариев
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

    elif guest_action - offset_menu == menu_items.index("Удалить всех мужчин"): # Далее все тоже самое по этому без комментариев
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

    elif guest_action - offset_menu == menu_items.index("Удалить всех женщин"):  # Далее все тоже самое по этому без комментариев
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

    elif guest_action - offset_menu == menu_items.index("Просмотр гостей"):

        # Можно отсортировать массив по возрасту в обратном порядке. Тогда само-собой взрослые будут в начале
        # Покопавшись - нашел такое решение:
        # guestList.sort(key = lambda x:x['ageGuest'], reverse=True)
        # но оно вне рамок урока.  По этому просто сздам новый отсортированный массив

        sortedList = []
        for i in range(len(guestList)):
            sortedList.append(guestList[i]['ageGuest'])
        sortedList.sort(reverse=True)
        for i in range(len(sortedList)):
            for j in range(len(guestList)):
                if sortedList[i] == guestList[j]['ageGuest']:
                    sortedList[i] = guestList[j]
                    break


        # print(sortedList)
        children_idx = 0
        print("--------------------------------------")
        print("Взрослые:")
        for i in range(len(sortedList)):
            guest = sortedList[i]
            if guest['ageGuest'] < 18:
                children_idx = i
                break
            print("--------------------------------------")
            print(f"Имя гостя - {guest['nameGuest']}")
            print(f"Возраст гостя - {guest['ageGuest']}")
            print(f"Пол гостя - {guest['genderGuest']}")
            print(f"Номер гостя - {guest['numberGuest']}")
            print(f"id - {guest['id']}")
        print("--------------------------------------")
        print("Дети:")
        for i in range(children_idx,len(sortedList)):
            guest = sortedList[i]
            # if guest['ageGuest'] < 18: break
            print("--------------------------------------")
            print(f"Имя гостя - {guest['nameGuest']}")
            print(f"Возраст гостя - {guest['ageGuest']}")
            print(f"Пол гостя - {guest['genderGuest']}")
            print(f"Номер гостя - {guest['numberGuest']}")
            print(f"id - {guest['id']}")

        nextGuest = False
        while nextGuest == False:
            nextGuest = (len(input("Посмотрели? Нажмите Enter> ")) == 0)

    elif guest_action - offset_menu == menu_items.index("Закончить"):
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
