"""
Случилась глобальная переделка - Сделалкласс RegistrationMenu.
На данный момент он позволяет не просто вывести меню, но и является менеджером для работы с классами Users & Children
По этому список зарегестрированных пользователей переехал в него.
Основной список шаблона оставил на месте так как он имитирует внешние данные

Кроме того решил сделать табличный вывод списка пользователей - показалось не сложно. Основное решение придумалось в
классе - сделать метод дополняющий строку пробелами до необходимой длины - это позволит выводить строки в столбики.
Но по пути столкнулся с множественными непредвиденными проблемками, вариантами их решений и новыми идеями.
В итоге пришлось разработатьотдельный класс для вывода таблиц. Так как функционал меню и таблицы стали сильно
переплетаться, а мне бы хотелось иметь универсальный инструмент на будущее. По этому пришлось разделить на два класса.
Теперь таблицей можно пользоваться как принтом, и можно ралзвивать ее функционал по мере необходимости
Для теста таблицы понадобились дополнительные поля, по этому пришлоь немного поменять User
метод create_user_list пока что является тестовым по тому не очень красив, и видимо таковым еще на долго останется.

Код менялся непрерывно, что то я комментировал, нв какой то момент бросил, так что в коде могут встретиться дубликаты
коментариев, или коментарии от перемещенного кода. По этому решил здесь описать суть проделанной работы.
Метод меню разрабатывал ранее. Здесь его только применил
"""
import random
from datetime import date

# from Home.dz16.main import RegistrationMenu
# rm = RegistrationMenu()

base_list = [
    {
        "firstname": "Николай",
        "lastname": "Меньшиков",
        "birthday": "27.10.1980",
        "gender": "Мужской",
        "login": "Niiik27",
        "password": "12345",
    },
    {
        "firstname": "Денис",
        "lastname": "Кириллов",
        "birthday": "01.06.2001",
        "gender": "Мужской",
        "login": "Denis161",
        "password": "54321",
    },
    {
        "firstname": "Екатерина",
        "lastname": "Исаева",
        "birthday": "25.10.2000",
        "gender": "Женский",
        "login": "Ekaterina25",
        "password": "11111",
    },
    {
        "firstname": "Ольга",
        "lastname": "Владимирова",
        "birthday": "22.11.1999",
        "gender": "Женский",
        "login": "Olya22",
        "password": "22222",
    },
    {
        "firstname": "Кирилл",
        "lastname": "Кириллов",
        "birthday": "17.11.2006",
        "gender": "Мужской",
        "login": "Kirillooo",
        "password": "55555",
    },
]


class User:
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        self.user_id = user_id
        self.rating = random.randint(1, 100)
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        self.status = "user"
        self.blocked = False

    def get_str_status(self):
        if self.status == "user":
            return "пользователь"
        elif self.status == "moderator":
            return "модератор"
        elif self.status == "admin":
            return "админ"

    def get_str_gender(self):
        if self.gender.lower() == "мужской":
            return "\u2642"
        elif self.gender.lower() == "женский":
            return "\u2640"

    def update_firstname(self, new_name):
        self.firstname = new_name

    def update_lastname(self, new_name):
        self.lastname = new_name

    def update_birthday(self, new_birth):
        self.birthday = new_birth

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_login(self, new_login):
        self.login = new_login

    def update_password(self):
        new_password = ""
        while new_password != self.password or new_password == "":
            new_password = input(f"Введите старый пароль> ")
        self.password = new_password

    def get_user_age(self):
        current_date = date.today().timetuple()
        current_year = current_date.tm_year
        current_month = current_date.tm_mon
        current_day = current_date.tm_mday

        birth_date = self.birthday.split(".")
        birth_year = int(birth_date[2])
        birth_month = int(birth_date[1])
        birth_day = int(birth_date[0])

        return int(current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day)))

    def to_table(self):
        return [
            str(self.user_id),
            f"{self.firstname} {self.lastname}",
            self.get_str_gender(),
            self.login,
            self.birthday,
            str(self.get_user_age()),
            self.status,
            f"{'Заблокирован' if self.blocked else 'ОК'}",
            self.password,
            self.rating
        ]

    def show_menu(self) -> int:
        return self.create_menu(["Редактировать профиль", "Удалиться", "Стать модератором", "Стать админом", "Выход"],
                                "Меню пользователя")

    def callback_menu(self, choice: int):
        ...

    def create_menu(self, menu_list: list, msg: str = "") -> int:
        """
        Метод принимает список пунктов меню, и строку для названия или сообщения меню
        Выводит сообщение и само меню с пронумерованными пунктами.
        Не позволяет сделать вывбор вне диапазона меню
        Возвращает int соответствующий пункту меню
        :param self:
        :param menu_list: list
        :param msg: str
        :return: int
        """

        menu_txt = ""
        for i in range(len(menu_list)):
            menu_txt += f"{i + 1} - {menu_list[i]}\n"
        choice = input(f"{msg}>>\nВыберите действие:\n{menu_txt}> ")
        while True:
            if not choice.isdigit():
                print(f"Допустим тольлько числовой ввод!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")
            elif 1 <= int(choice) <= len(menu_list):
                return int(choice)
            else:
                print(f"Число должно быть в диапазоне от 1 до {len(menu_list)}!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")

    def show(self):
        print(f"Данные пользователя{self.firstname}:")
        print(f"id: {self.user_id}")
        print(f"Рейтинг:{self.rating}")
        print(f"Имя: {self.firstname}")
        print(f"фамилия: {self.lastname}")
        print(f"День рождения: {self.birthday}")
        print(f"Возраст: {self.get_user_age()}")
        print(f"Пол: {self.gender}")
        print(f"Логин: {self.login}")
        print(f"Пароль: {self.password}")
        print(f"Статус: {self.status}")
        print(f"Состояние {'Заблокирован' if self.blocked else 'OK'}")


class Moderator(User):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password)
        self.status = "moderator"

    # def blocking_user(self, user_id, menu):
    #     for i in range(len(menu.registered_users)):
    #         user: User = menu.registered_users[i]
    #         if user.user_id == user_id:
    #             user.blocked = True
    #             menu.user_list_fields[i][menu.table_view.headers.index("Состояние")] = "Заблокирован"
    #             menu.table_view.build_tab(menu.user_list_fields)
    #             break
    #
    # def unblocking_user(self, user_id, menu):
    #     for i in range(len(menu.registered_users)):
    #         user: User = menu.registered_users[i]
    #         if user.user_id == user_id:
    #             user.blocked = False
    #             menu.user_list_fields[i][menu.table_view.headers.index("Состояние")] = "OK"
    #             menu.table_view.build_tab(menu.user_list_fields)
    #             break

    def blocking_users(self, user_ids, menu):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for i in range(len(menu.registered_users)):
                registered_user: User = menu.registered_users[i]
                if blocked_id == registered_user.user_id:
                    if registered_user.status == "admin":
                        print("Вы не можете заблокировать админа")
                        continue
                    elif registered_user.status == "moderator":
                        print("Вы не можете заблокировать другого модератора. Обратитесь к администратору")
                        continue
                    registered_user.blocked = True
                    menu.user_list_fields[i][menu.table_view.headers.index("Состояние")] = "Заблокирован"
                    break
        menu.table_view.build_tab(menu.user_list_fields)

    def unblocking_users(self, user_ids, menu):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for i in range(len(menu.registered_users)):
                registered_user: User = menu.registered_users[i]
                if blocked_id == registered_user.user_id:
                    registered_user.blocked = False
                    menu.user_list_fields[i][menu.table_view.headers.index("Состояние")] = "OK"
                    break
        menu.table_view.build_tab(menu.user_list_fields)

    def show_menu(self) -> int:
        return self.create_menu(["Заблокировать - укажите id пользователей через пробел",
                                 "Разблокировать - укажите id пользователей через пробел", "Выход"], "Меню модератора")

    def callback_menu(self, choice: int):
        if choice == 3:
            print("Досвидания")
            return False
        regMenu.show_users()
        user_id = input("Введите id пользователя: ")
        if choice == 1:
            self.blocking_users(user_id, regMenu)
        elif choice == 2:
            self.unblocking_users(user_id, regMenu)

        return True


class Admin(Moderator):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password)
        self.status = "admin"

    def delete_user_list(self, user_list):
        user_list.clear()
        print("База данных пустая")

    def show_menu(self) -> int:
        return self.create_menu(
            ["Заблокировать", "Разблокировать", "Добавить пользователя", "Удалить пользователя", "Выход"],
            "Меню админа")

    def callback_menu(self, choice: int):
        if choice == 5:
            print("Досвидания")
            return False
        regMenu.show_users()
        user_id = input("Введите id пользователя: ")
        if choice == 1:
            entered_user.blocking_user(user_id, regMenu)
        elif choice == 2:
            entered_user.unblocking_user(user_id, regMenu)
        elif choice == 3:
            entered_user.blocking_user(user_id, regMenu)
        elif choice == 4:
            entered_user.unblocking_user(user_id, regMenu)

        return True


class RegistrationMenu:
    def __init__(self):
        """Идея создания таблицы потребовала сначала измерения ее параметров, использования результатов измерения,
        а раз мы сначала измеряем, то было бы неплохо сохранить ширину таблицы. Но более эффективно будет сохранить
        горизонтальную линию, а из нее получить ширину - не проблема.
        Вообще тема таблицы сильно раздулась, и было бы не плохо создать для нее отдельный класс. Если успею
        то сделаю, но пока работаю в этом классе
        """
        self.registered_users = []
        self.line: str = "|"
        self.width_columns = None
        # self.table_view = TableView(
        #     {"№": "center", "id": "left", "Имя": "left", "Логин": "left", "День рождения": "center",
        #      "Возраст": "center", "Статус": "center", "Состояние": "center", "Пароль": "right",
        #      "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")
        self.table_view = TableView(
            {"№": "center", "id": "left", "Имя": "left", "Пол": "center", "Логин": "left", "День рождения": "center",
             "Возраст": "rating.15.*", "Статус": "center", "Состояние": "center", "Пароль": "right",
             "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")

        self.user_list_fields = []

    def create_user_list(self):
        """
        Здесь заполняем список пользователей что бы было хоть что то, и не приходилось каждый раз создавать список
        По этому пришлось вклбчить в код детали таблицы
        """

        self.registered_users.append(Admin(
            user_id="10",
            # Если id int типа вместо строкового то пользователя нельзя обнаружить по id, если искать строки
            firstname=base_list[0]["firstname"],
            lastname=base_list[0]["lastname"],
            birthday=base_list[0]["birthday"],
            gender=base_list[0]["gender"],
            login="qqq",
            password="qqq"))

        self.registered_users.append(Moderator(
            user_id="100500",
            firstname=base_list[1]["firstname"],
            lastname=base_list[1]["lastname"],
            birthday=base_list[1]["birthday"],
            gender=base_list[1]["gender"],
            login="www",
            password="www"))

        for i in range(2, len(base_list)):
            self.registered_users.append(User(
                user_id=self.create_id(),
                firstname=base_list[i]["firstname"],
                lastname=base_list[i]["lastname"],
                birthday=base_list[i]["birthday"],
                gender=base_list[i]["gender"],
                login=base_list[i]["login"],
                password=base_list[i]["password"]))

        """После появления новых пользователей нужно задать параметры таблицы"""

        for i in range(len(self.registered_users)):
            user: User = self.registered_users[i]
            line = user.to_table()
            line.insert(0, i + 1)
            self.user_list_fields.append(line)

        self.table_view.build_tab(self.user_list_fields)

    def create_id(self, user_id_len=8):
        """
        В каких то старых домашках делал создатель ид. Теперь решил записатьего ввиде метода,
        но пока не решил - использовать или нет. Так что пусть будет. Дальше будет видно
        :param user_list:list
        :return:
        """
        new_id_user = ""
        id_symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        # id_symbols = "1234567890"  # упростил до цифр
        while True:
            for _ in range(user_id_len):
                symbol_index = random.randint(0, len(id_symbols) - 1)
                new_id_user += id_symbols[symbol_index]

            for user in self.registered_users:
                if user.user_id == new_id_user:
                    new_id_user = ""
                    break
            if len(new_id_user) != 0:
                break

        return new_id_user

    def check_in(self):
        try_count = 5
        while try_count:
            my_login = input("Введите Логин ")
            my_pass = input("Введите пароль ")
            for i in range(len(self.registered_users)):
                registered_user = self.registered_users[i]
                if my_login == registered_user.login and my_pass == registered_user.password:  # только попав сюда - можно считать что логин существует
                    return registered_user
            try_count -= 1
            print(f"Логин или пароль не верный, осталось {try_count} чтобы войти")
        print("Отказано в доступе")
        return None

    def show_menu(self, menu_list: list, msg: str = "") -> int:
        """
        Метод принимает список пунктов меню, и строку для названия или сообщения меню
        Выводит сообщение и само меню с пронумерованными пунктами.
        Не позволяет сделать вывбор вне диапазона меню
        Возвращает int соответствующий пункту меню
        :param self:
        :param menu_list: list
        :param msg: str
        :return: int
        """
        print()
        menu_txt = ""
        for i in range(len(menu_list)):
            menu_txt += f"{i + 1} - {menu_list[i]}\n"
        choice = input(f"{msg}\nВыберите действие:\n{menu_txt}> ")
        while True:
            if not choice.isdigit():
                print(f"Допустим тольлько числовой ввод!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")
            elif 1 <= int(choice) <= len(menu_list):
                return int(choice)
            else:
                print(f"Число должно быть в диапазоне от 1 до {len(menu_list)}!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")

    def show_users(self):
        self.table_view.print_tab(self.user_list_fields)

    def blocking_users(self, user_list):
        """
        Пока не участвующий метод. сохранил его на будущеее
        :param user_list:
        :return:
        """
        # txt_user_list = ""
        blocked_user_list = []
        self.show_users()
        input_user_id = int(input("Введите id пользователя для блокировки "))
        for i in range(len(user_list)):
            if self.status == "moderator":
                if input_user_id == user_list[i].user_id and user_list[i].status != "moderator" and user_list[
                    i].status != "admin":
                    if user_list[i].blocked == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        user_list[i].blocked = True
                        print("Пользователь упешно заблокирован")
                        break
            elif self.status == "admin":
                if input_user_id == user_list[i].user_id:
                    if user_list[i].blocked == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        user_list[i].blocked = True
                        print("Пользователь упешно заблокирован")
                        break
        blocked_user_list = []
        for i in range(len(user_list)):
            user: User = user_list[i]
            blocked_user_list.append(user.to_table())
        self.print_tab(self.table_head, blocked_user_list, "Таблица заблокированных пользователей")

    def check_login(self, my_login) -> bool:
        while len(my_login) == 0:
            print("Поле не может быть пусто!")
            my_login = input("Введите Логин ")
        for user in self.registered_users:
            if my_login == user.login:
                return True
        return False

    def input_field(self, field_name) -> str:
        name = input(f"Введите {field_name} ")
        while len(name) == 0:
            print("Поле не может быть пусто!")
            name = input(f"Введите {field_name} ")
        return name

    def input_gender(self) -> str:
        gender = input("Введите пол ")
        while len(gender) == 0:
            print("Поле не может быть пусто!")
            gender = input("Введите пол ")
        gender = gender.lower()
        if gender.startswith("м") or gender.startswith("m") or gender.startswith("v") or gender.startswith(
                "ь") or gender.startswith("1"):
            return "Мужской"
        elif gender.startswith("ж") or gender.startswith("w") or gender.startswith(";") or gender.startswith("2"):
            return "Женский"

    def input_birthday(self) -> str:
        birthday = input("день рождения в формате ДД.ММ.ГГГГ ")
        if not birthday or birthday.count(".") == 0:
            birthday = "01.01.1970"
        return birthday

    def input_login(self) -> str:
        while True:
            my_login = input("Введите Логин ")
            if not self.check_login(my_login):
                return my_login
            print("Такой логин уже занят!")

    def check_pass(self, my_login) -> dict | None:
        if self.check_login(my_login):
            my_pass = input("Введите Пароль ")
            while len(my_pass) == 0:
                print("Поле не может быть пусто!")
                my_pass = input("Введите Пароль")

            for usr in self.registeredUsers:
                if usr["myLogin"] == my_login:
                    if my_pass == usr["myPass"]:
                        return usr
                    else:
                        return None
            return None

    def input_pass(self, password_name=''):
        password = input("Введите пароль " if not password_name else password_name)
        while len(password) == 0:
            print("Поле не может быть пусто!")
            password = input("Введите пароль ")
        return password

    def reister_new_user(self):
        while True:
            new_user = User(
                user_id=regMenu.create_id(),
                firstname=self.input_field("имя"),
                lastname=self.input_field("фамилию"),
                birthday=self.input_birthday(),
                gender=self.input_gender(),
                login=self.input_login(),
                password=self.input_pass("Придумайте пароль: "))
            new_user.show()

            if not input("Enter - Подтвердить "):
                self.registered_users.append(new_user)
                line = new_user.to_table()
                line.insert(0, len(self.registered_users))
                self.user_list_fields.append(line)
                self.table_view.build_tab(self.user_list_fields)

                return new_user
            else:
                print("Начните регистрацию заново ")


class TableView:
    def __init__(self, table_head: dict, tab_name: str = None, padding: int = 1):
        """
        Табличный вывод данных - таблица рисуется на основе шапки, и затем в нее передается тело.
        Так сделано, что бы можно было узнать ширину таблицы до ее отображения, что бы можно было вывести дополнительное
        инфо о таблице или ее заголовок.
        Шапка принимается ввиде словаря - ключи - имена полей, значения - то, по какому краю выравнивать содержимое полей
        Значения могут быть left, center, right и rating/rating.x/rating.x.y
        Если у поля значение rating, то поле должно быть цифровым x - ширина ячейки для рейтинго, y - символ, которым
        показывать рейтинг.
        Таблица вертикальная - горизонтальные линии содержат символы вертикальных линий - так легче васпринимается, но
        это усложнило код, и вообще привело к созданию таблицы с данным функционалом.
        А так же - значение padding регулирует отступы только справа и слева

        :param table_head:dict - словарь полей таблицы
        :param tab_name: str - название таблицы
        :param padding:int - отступы от краев таблицы
        """

        self.table_head: dict = table_head
        self.headers: list = list(table_head.keys())
        self.tab_name: str = tab_name
        self.padding: int = padding
        self.rating_symbol: str = "\u2588"
        self.rating_len: int = 50
        """
        Идея создания таблицы потребовала сначала измерения ее параметров, использования результатов измерения,
        а раз мы сначала измеряем, то было бы неплохо сохранить ширину таблицы. Но более эффективно будет сохранить
        горизонтальную линию, а из нее получить ширину - не проблема.
        Вообще тема таблицы сильно раздулась, и было бы не плохо создать для нее отдельный класс. Если успею
        то сделаю, но пока работаю в этом классе
        """
        """
        Все таки творческий процесс пока не позволяет удалять старые коменты,
        Все таки пришлось добраться до создания класса таблицы, а то близится какя то путаница,
        а возможности таблицы стихийно расширяются, и методы и правила так же меняются
        
        Теперь примерно такая идея: 
        Создаем таблицу на основе шапки, если есть контент, то его тоже принимаем/обрабатываем.
        в дальнейшем можем добавлять/удалять записи (в соответствии с шапкой - здесь открываются возмможности для
        автоматизации приема и контроля данных)
        
        Таблица не будет уметь обслуживать пользователей, но пользователей можно подстроить для работы с таблицей
        Можно даже создавать пользователей на основе данных в таблице, или забирать данные полей таблицы
        Пока не все будет реализовано так как непонятен объем работы
        
        """
        self.line: str = "|"
        self.width_columns: list = None

    # def show_menu(self, menu_list: list, msg: str = "") -> int:
    #     """
    #     Пожалуй было бы правильно придать функционал таблице.... тогда тоблица должна принимать какие то данные
    #     не просто для распечатки, а для хранения и модификации
    #
    #     Это дополнительный функционал так что не помешает использованию, таблицы в качестве альтернативного принта
    #
    #     Метод принимает список пунктов меню, и строку для названия или сообщения меню
    #     Выводит сообщение и само меню с пронумерованными пунктами.
    #     Не позволяет сделать вывбор вне диапазона меню
    #     Возвращает int соответствующий пункту меню
    #     :param self:
    #     :param menu_list: list
    #     :param msg: str
    #     :return: int
    #     """
    #     print()
    #     menu_txt = ""
    #     for i in range(len(menu_list)):
    #         menu_txt += f"{i + 1} - {menu_list[i]}\n"
    #     choice = input(f"{msg}>>\nВыберите действие:\n{menu_txt}> ")
    #     while True:
    #         if not choice.isdigit():
    #             print(f"Допустим тольлько числовой ввод!")
    #             choice = input(f"Выберите действие:\n{menu_txt}> ")
    #         elif 1 <= int(choice) <= len(menu_list):
    #             return int(choice)
    #         else:
    #             print(f"Число должно быть в диапазоне от 1 до {len(menu_list)}!")
    #             choice = input(f"Выберите действие:\n{menu_txt}> ")

    def make_cell(self, my_string: str, cell_len: int, symbol: str = " ", position="center", offset=0):
        """
        Метод созает из пробелов строку нужной длины, и вписывает в середину нужную строку.
        Получается, что все строки  будут не меньше заданной длины, что позволит красиво их разместить в столбик

        :param my_string:
        :param cell_len:
        :param symbol:
        :position:int 1-left, 2-center, 3-right
        :return:
        """
        if position == "rating":
            position = "left"
        start_offset = ((cell_len - len(str(my_string))) // (2 - (position == "right"))) * (position != "left") + \
                       offset * (position == "left") - offset * (position == "right")
        end_offset = cell_len - len(str(my_string)) - start_offset
        return f"{symbol * start_offset}{my_string}{symbol * end_offset}"

    def raiting_view(self, cell_width: int, fill_percent: int, symbol: str = "\u2588"):
        len_digit = 3
        symbols_num = int((cell_width - len_digit) / 100 * int(fill_percent))
        raiting_line = f"{self.make_cell(str(fill_percent), len_digit, ' ', 'left')} {symbol * symbols_num}"
        return self.make_cell(raiting_line, cell_width, " ", 'left', 1)

    def build_tab(self, content: list):
        """
        Метов выводит таблицу данных.

        :param tab_head: list Массив заголовков столбцов
        :param content: list Массив массивав данных таблицы
        :param tab_name: str Название таблицы
        :param padding: int Размер полей вокруг текста в таблице

        :return: None
        """
        """
        Немного поизучал методы str
        Основная идея - приментиь ljust, rjust, center. Но нужене только center
        Сначала хотел свой метод написать, но немного покопавшись - нашел то что нужнно.
        Проблема метода в том что мы не знаем ширину текста для вывода в ячейку. По этому ячейки должны быть либо достаточно
        широкими, что бы обеспечить максимальную возможность для отображения длинных строк, либо они должны быть адаптивными
        тогда нам потребуется сначала измерить длину каждой строки, и на основании максимальной принять ширину столбца
        Конечно выбрал второй вариант, так как если решить эту задачу, то в будущем у меня будет удобный инструмент
        Другая проблема в том что планировалось просто распечатать поля юзера,требовалось упрощение процесса и не
        требовалось универсальности. Теперь же нарисовался довольно сложный код и было бы жалко его отдавать только под
        использование юзером. По этому во входных параметрах он принимает линейный массив для заголовков таблицы,
        и прямоугольный массив самих данных, при этом ширина таблицы ограничена количеством заголовков, и если данных
        будет больше, то они не выведутся, если данных будет меньше, то таблица заполнится слева на право,
        а нехватка данных будет отображена пустыми ячейками
        Так же стоит отметить что таблица вертикально-ориентирована - символы вертикальной черты присутствуют в
        горизонтальных линиях. Это потребовало усложнения кода, но сделало таблицу более читабельной.
        Для работы с юзером придется его обучить выдавать текстовые поля
        """
        self.line: str = "|"
        self.width_columns = []

        list_of_width_cells = []
        width_cells = []
        """
        Сначала измерим ячейки и соберем информацию о них в общий массив массивов
        затем из каждого массива выберем максимум. Это нужно что бы определить где рисовать вертикальные линии.
        Этот код можно было сделать проще, если бы ширина столбцов выбиралась на основе только лишь заголовков,
        но стремление к компактности и легкости восприятия - потребовали усложнений
        """
        for col_name in self.table_head:
            width_cells.append(self.padding + len(col_name) + self.padding)
        list_of_width_cells.append(width_cells)
        for user_line in content:
            """
            На всякий случай увеличим количество ячеек в строке, если их меньше полей таблицы.
            Это защитит от ошибки индекса. Но такая ситуация не предполагается        
            """
            while len(user_line) < len(self.table_head):
                user_line.append("")
            width_cells = []
            """
            Пришлось сделать независимое преобразование в рейтинг на лету
            ценой двойной работы = преобразовывается для подсчета размера,
            и преобразовывается при выводе на экран
            это позволяет обновлять таблицу, иначе не получается рейтинг превратить в int
            Возможно нужно создать такой метод... но это будет уже в моменте оптимизации
            """
            for i in range(len(user_line)):
                cel_str = str(user_line[i])
                """ширина ячейки равна ширине записи плюс отступы по бокам"""
                if "rating" in self.table_head[self.headers[i]]:
                    cell_info = self.table_head[self.headers[i]].split(".")
                    rating_len = self.rating_len
                    rating_symbol = self.rating_symbol
                    if len(cell_info) > 1:
                        rating_len = int(cell_info[1])
                    if len(cell_info) > 2:
                        rating_symbol = cell_info[2]
                    # print(user_line)
                    # print(user_line[i])
                    # print(self.headers.index("Возраст"))
                    rating_max = int(max(content, key=lambda x: int(x[i]))[i])
                    # print(rating_max)
                    # print(rating_max)
                    # print(type(user_line[i]))
                    # print(type(rating_max))
                    rating_percent = int(int(user_line[i]) / rating_max * 100)
                    # print(self.headers[i],rating_percent)
                    cel_str = self.raiting_view(rating_len, rating_percent, rating_symbol)

                width_cells.append(self.padding + len(cel_str) + self.padding)

            """Для рейтинга нужно преобразовать число в количество символов в процентном соотношении"""

            list_of_width_cells.append(width_cells)
        """Здесь я хотел использовать функцию map, но что то не заладилось. Пришлось использовать генератор массива
            он выбырает из массива массивов массив с наибольшим значением в соответствующем поле, и берет этот максимум
            в итоге получается список ширин колонок
        """
        self.width_columns = [max(list_of_width_cells, key=lambda x: x[z])[z] for z in range(len(self.table_head))]
        """
        Здесь можно построить горизонтальную линию таблицы, потому что она не изменяемая, а при этом она даст
        информацию о ширине таблицы. Это может потребоваться для создания доплонительных записей-заголовков
        """

        for i in self.width_columns:
            self.line += "-" * i + "|"
        # return self.width_columns

    def print_tab(self, content: list):
        """
        Метов выводит таблицу данных.

        :param tab_head: list Массив заголовков столбцов
        :param content: list Массив массивав данных таблицы
        :param tab_name: str Название таблицы
        :param padding: int Размер полей вокруг текста в таблице

        :return: None
        """
        """
        Произошло разделение метода на измерение параметров и отрисовку таблицы.
        Это потребовалось что бы я мог привязываться к размерам таблицы не выводя ее на экран
        """
        field_str = "|"
        # self.width_columns = self.build_tab(tab_head, content, padding)
        """Немного страшноватое решение, но я вычитал, что с версии 3.6 словари хранят порядок добавления в словарь"""
        for i in range(len(self.headers)):
            field: str = self.headers[i]
            field_str += f"{self.make_cell(field, self.width_columns[i])}|"

        # print()
        if self.tab_name:
            print(self.make_cell(f" {self.tab_name} ", len(self.line), '*'))
        print("_" * len(self.line))
        print(self.line.replace("-", " "))  # Найти и понять суть метода очень просто, по этому использую его

        print(field_str)
        print(self.line)
        """Только здесь мы добрались до отображения данных таблицы"""
        for n in range(len(content)):
            user_line = content[n]
            field_str = "|"
            for i in range(len(self.headers)):
                field: str = user_line[i]
                """             
                немного поизвращался с привязками - что бы просмотреть как работает ячейка. Часть ячеек выравнены
                по левому краю, часть по середине, и пароль по правому
                за одно повысил читабельность таблицы так как имя фамилия лучше смотрятся выровненными по левому краю
                """
                if "rating" in self.table_head[self.headers[i]]:
                    cell_info = self.table_head[self.headers[i]].split(".")
                    rating_len = self.rating_len
                    rating_symbol = self.rating_symbol
                    if len(cell_info) > 1:
                        rating_len = int(cell_info[1])
                    if len(cell_info) > 2:
                        rating_symbol = cell_info[2]

                    rating_max = int(max(content, key=lambda x: int(x[i]))[i])
                    rating_percent = int(int(user_line[i]) / rating_max * 100)

                    field = self.raiting_view(rating_len, rating_percent, rating_symbol)

                field_str += f"{self.make_cell(field, self.width_columns[i], ' ', self.table_head[self.headers[i]], self.padding)}|"
            print(field_str)
            print(self.line)


regMenu = RegistrationMenu()
regMenu.create_user_list()

print(regMenu.table_view.make_cell(
    " Тестовая строка из-за которой пришлось перелопатить и резделить таблицу на измерение и отрисовку ",
    len(regMenu.table_view.line), "|"))

print(regMenu.table_view.make_cell(" Показываю таблицу пользователей, что бы можно было выбрать логин/пароль для входа",
                                   len(regMenu.table_view.line), "|"))
regMenu.show_users()  # Придется сначала увидеть список пользователей что бы решить под кем входить

entrie_type = regMenu.show_menu(["Вход", "Регистрация"], "Войдите или зарегистрируйтесь")
if entrie_type == 1:
    entered_user = regMenu.check_in()
else:
    entered_user = regMenu.reister_new_user()
    regMenu.show_users()

print()
print(f"Добро пожаловать {entered_user.get_str_status()} {entered_user.firstname} {entered_user.lastname}")

while entered_user.callback_menu(entered_user.show_menu()):
    regMenu.show_users()
