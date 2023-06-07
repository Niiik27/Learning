blackList = ["я", "коля", "денис"]
guestList = []
menu_items = ["Добавить гостя", "Удалить гостя", "Просмотр гостей", "Закончить"]
offset_menu = 1
finish_range = [1, 10]

while True:
    strItems = ""
    for i in range(0, len(menu_items) - 1 + int(finish_range[0] < len(guestList) < finish_range[1])):
        strItems += f"{i + offset_menu} - {menu_items[i]}\n"
    print("Регистрация гостей: ")
    guest_action = int(input(f"Выберите действие:\n{strItems}> "))
    if guest_action == 0 + offset_menu:
        guest_name = input(f"Введите имя нового гостя:> ")
        if guest_name not in blackList:
            guestList.append(guest_name)
        else:
            print("Этого человека нельзя приглашать! ")
    elif guest_action == 1 + offset_menu:
        print(f"Список гостей: {guestList}\n")
        del_guest = input("Введите имя удаляемого гостя:> ")
        guestList.remove(del_guest)
        print(f"Список гостей: {guestList}\n")
    elif guest_action == 2 + offset_menu:
        print(f"Список гостей: {guestList}\n")
    # elif guest_action == 3+offset_menu:
    #     if finish_range[0]<len(guestList)<finish_range[1]:
    #         offer = input("Прекратить регистрацию?> ")
    #         if offer == "y": break

    # Мне кажется правильнее было бы объеденить условия выхода из цикла в свою группу
    if finish_range[0] < len(guestList) < finish_range[1]:
        if guest_action == 3 + offset_menu:
            break
    elif len(guestList) >= finish_range[1]:
        print(f"Список гостей: {guestList}\n")
        break
