"""
С ПОМОЩЬЮ ЦИКЛОВ и ФУНКЦИЙ
СОЗДАТЬ json ПРИГЛАШЕННЫХ ГОСТЕЙ НА МЕРОПРИЯТИЕ ФУНКЦИОНАЛ
1. Метод добавления в список (указать только имя гостя) после ввода вернуться в
выбор методов
2. Метод удаления гостя (по номеру или по имени) + этот гость улетает в блэк лист
3. Просмотр гостей
4. Если гостей больше 5 и меньше 10, то предложить пользователю закончить цикл
Нельзя приглашать более 10 гостей и не меньше (Тут видимо недописано количество. Условно будет 5)
5. Доп задание - Создать массив с именами тех людей которых нельзя приглашать +
хорошее оформление + Комментарии
"""
import json


def num_input(msg, start=-1, end=-1) -> int:
    """
        Фильтр на ввод - допускает только ввод чисел, в заданном диапазоне
    """
    num = input(f"{msg}:> ")
    while True:
        if not num.isdigit():
            print("Допустим тольлько числовой ввод!")
            num = input(f"{msg}:> ")
            continue
        elif -1 < int(num) < start:
            print(f"Число не должно быть меньше {start}")
            num = input(f"{msg}:> ")
            continue
        elif -1 < end < int(num):
            print(f"Число не должно быть больше {end}")
            num = input(f"{msg}:> ")
            continue
        return int(num)


def show_menu(menu_list, msg) -> int:
    """
    Разлелепил меню на меню и фильтр ввода, так как фильтр потребуется отдельно
    :param menu_list:
    :param msg:
    :return:
    """
    start_number = 1
    menu_txt = ""
    for i in range(len(menu_list)):
        menu_txt += f"{i + start_number} - {menu_list[i]}\n"
    return num_input(f"{msg}\nВыберите:\n{menu_txt}", start_number, len(menu_list))


def show_list(menu_list, msg) -> int:
    """
    Просмотр списка с нумерацией элементов
    :param menu_list:
    :param msg:
    :return:
    """
    start_number = 1
    menu_txt = f"{msg}\n"
    for i in range(len(menu_list)):
        menu_txt += f"{i + start_number} - {menu_list[i]}\n"
    print(menu_txt)


guest_list = []
guest_list2 = []
blacklist = []
menu_list = ["Добавить гостя", "Добавить гостя в блэклист", "Посмотреть список гостей", "Посмотреть блэклист"]

min_num = 5
max_num = 10
num_items = len(menu_list)
while len(guest_list) < max_num:
    # Пункт выхода добавляется после добавления минимального количества человек
    if num_items == len(menu_list) and len(guest_list) >= min_num:
        menu_list.append("Выход")
    choice = show_menu(menu_list, "Меню добавления/удаления гостей")
    if choice == 1:
        new_guest = input("Введите имя нового гостя:> ")
        if new_guest not in blacklist:
            """
            Чтобы создать json необязательно запихивать его в словать, прежде чем добавить в список
            по этому просто добавляю в список. json скушает. Если делать через словарь, 
            то потребуется придумывать какое то значение для гостя. Например это может быть флаг блокировки,
            но пока понял задачу - как отдельное создание блэклиста, к тому же перед выводом его все равно потребуется
            создавать...
            
            Впрочем обычный список выглядит очень скучно, так что сделаю параллельный вариант
            
            """
            guest_list.append(new_guest)
            # Параллельный список со словарями
            guest_list2.append({new_guest: "invited"})
        else:
            print("Этого нельзя приглашать!!!")
    elif choice == 2:
        # Выбираем способ удаления
        way = show_menu(["по номеру", "по имени"], "Способ удаления")
        if way == 1:
            guest_id = num_input("Укажите номер гостя", 1, len(guest_list))
            blacklist.append(guest_list[guest_id - 1])
            guest_list.pop(guest_id - 1)
            # Параллельный список со словарями
            dict_name = guest_list2[guest_id - 1]
            name = list(dict_name.keys())[0]
            dict_name[name] = "Blocked"

        else:
            guest_name = input("Введте имя гостя:> ")
            blacklist.append(guest_name)
            guest_list.remove(guest_name)
            # Параллельный список со словарями
            for g in guest_list2:
                g: dict
                key_name = list(g.keys())[0]
                if key_name == guest_name:
                    g[key_name] = "Blocked"
                    break
    elif choice == 3:
        show_list(guest_list, "Список гостей")
        # Параллельный список со словарями
        # Для параллельного массива не стал делать отдельных методов, так как он просто на один раз - посмотреть
        for guest in guest_list2:
            key_name = list(guest.keys())[0]
            value = guest[key_name]
            # Может быть можно не выделываться с условиями, а просто показывать весь список с разными статусами
            if value != "Blocked":
                print(f"{key_name} - {value}")
    elif choice == 4:
        show_list(blacklist, "Черный список")
        # Параллельный список со словарями
        for guest in guest_list2:
            key_name = list(guest.keys())[0]
            value = guest[key_name]
            if value == "Blocked":
                print(f"{key_name} - {value}")
    elif choice == 5:
        print(f"Добавление гостей закончено. Приглашено {len(guest_list)} гостей")
        break
    if len(guest_list) == max_num:
        print(f"Список гостей полон. Приглашено все {max_num} человек")
        print(f"В черном списке {len(blacklist)} человек")
        break
guest_JASON = json.dumps(guest_list, ensure_ascii=False)
guest_list = json.loads(guest_JASON)
print(guest_JASON, type(guest_JASON))
print(guest_list, type(guest_list))

guest_JASON2 = json.dumps(guest_list2, ensure_ascii=False)
guest_list2 = json.loads(guest_JASON2)
print(guest_JASON2, type(guest_JASON2))
print(guest_list2, type(guest_list2))
