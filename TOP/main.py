"""
mongodb
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
import datetime
import random
from datetime import date


# from Home.dz16.main import RegistrationMenu
# rm = RegistrationMenu()
class Menu:
    """
    Слишком часто требуется меню. С ограничениями на ввод. Для этого нужен отдельный метод.
    Но оно нужно в разных контекстах, и тогда придется дублировать метод в разные классы.
    По этому создал класс для данного метода. За одно это позволит сразу сохранить поля меню
    """

    def __init__(self, menu_list: list, msg: str = ""):
        self.menu_list = menu_list
        self.msg = msg

    def show(self) -> int:
        """
        Метод принимает строит меню, и защищает от неправильного ввода
        :return: int
        """
        print()
        menu_txt = ""
        for i in range(len(self.menu_list)):
            menu_txt += f"{i + 1} - {self.menu_list[i]}\n"
        choice = input(f"{self.msg}\nВыберите действие:\n{menu_txt}> ")
        while True:
            if not choice.isdigit():
                print(f"Допустим тольлько числовой ввод!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")
            elif 1 <= int(choice) <= len(self.menu_list):
                return int(choice)
            else:
                print(f"Число должно быть в диапазоне от 1 до {len(self.menu_list)}!")
                choice = input(f"Выберите действие:\n{menu_txt}> ")


class TableView:
    def __init__(self, table_head: dict, tab_name: str = None, padding: int = 1):
        """
        Табличный вывод данных - таблица разделена на построение и вывод. Это необходимо для того что бы можно было
        до вывода таблицы вывести дополнительный заголовок или строку в стиле таблицы - с обрамлением на всю ширину
        Для работы таблицы необходима шапка - словарь в формате имя_колонки:выравнивание left,right,center,raiting.


        :param table_head:dict - словарь полей таблицы
        :param tab_name: str - название таблицы
        :param padding:int - отступы от краев таблицы
        """

        self.table_head: dict = table_head
        self.headers: list = list(table_head.keys())
        self.tab_name: str = tab_name
        self.padding: int = padding
        self.rating_symbol: str = "\u2588"
        self.rating_len: int = 40
        self.tab_str: str = ""
        self.line: str = ""
        self.width_columns: list = []
        self.content: list = []

    @staticmethod
    def make_cell(my_string: str, cell_len: int, symbol: str = " ", position="center", offset=0):
        """
        Метод дополняет строку символами до нужной длины
        :param my_string:
        :param cell_len:
        :param symbol:
        :param position:
        :param offset:
        :return:
        """
        if position == "rating":
            position = "left"
        start_offset = ((cell_len - len(str(my_string))) // (2 - (position == "right"))) * (
                position != "left") + offset * (position == "left") - offset * (position == "right")
        end_offset = cell_len - len(str(my_string)) - start_offset
        return f"{symbol * start_offset}{my_string}{symbol * end_offset}"

    def raiting_view(self, cell_width: int, fill_percent: int, original_value: int, symbol: str = "\u2588"):
        """
        Метод выводит строку из исходного числа в и символов графика в процентном соотношении от общей ширины ячейки
        :param cell_width:
        :param fill_percent:
        :param original_value:
        :param symbol:
        :return:
        """
        len_digit = 3
        symbols_num = int((cell_width - len_digit) / 100 * int(fill_percent))
        raiting_line = f"{self.make_cell(str(original_value), len_digit, ' ', 'left')} {symbol * symbols_num}"
        return self.make_cell(raiting_line, cell_width, " ", 'left', 0)

    def build_tab(self):
        """
        Метов строит таблицу из шапки и данных для дальнейшего вывода.
        возвращяет свой инстанс. Так удобнее вызывать принт. В целом удалось сделать задуманное, и больше нет
        желания как то менято код, по этому оставлю его без коментариев, хоть он и самый сложный в этом классе


        :return: self
        """
        self.line: str = "|"
        list_of_width_cells = []
        width_cells = []
        for col_name in self.table_head:
            width_cells.append(self.padding + len(col_name) + self.padding)
        list_of_width_cells.append(width_cells)
        for user_line in self.content:

            while len(user_line) < len(self.table_head):
                user_line.append("")
            width_cells = []

            for i in range(len(user_line)):
                cel_str = str(user_line[i])
                if "rating" in self.table_head[self.headers[i]]:
                    rating_len = self.rating_len
                    cell_info = self.table_head[self.headers[i]].split(".")
                    if len(cell_info) > 1:
                        rating_len = int(cell_info[1])
                    cel_str = self.rating_symbol * rating_len

                width_cells.append(self.padding + len(cel_str) + self.padding)
            list_of_width_cells.append(width_cells)
        width_columns = [max(list_of_width_cells, key=lambda x: x[z])[z] for z in range(len(self.table_head))]

        self.line = "|"
        for i in width_columns:
            self.line += "-" * i + "|"

        if self.tab_name:
            self.tab_str = self.make_cell(f" {self.tab_name} ", len(self.line), '*') + "\n"
        else:
            self.tab_str = "|"

        self.tab_str += "_" * len(self.line) + "\n"
        self.tab_str += self.line.replace("-", " ") + "\n"

        for i in range(len(self.headers)):
            field: str = self.headers[i]
            self.tab_str += f"|{self.make_cell(field, width_columns[i])}"

        self.tab_str += "|\n"
        self.tab_str += self.line.replace("-", "_") + "\n"

        for n in range(len(self.content)):
            user_line = self.content[n]
            self.tab_str += "|"
            for i in range(len(self.headers)):
                field: str = user_line[i]

                if "rating" in self.table_head[self.headers[i]]:
                    rating_symbol = self.rating_symbol
                    cell_info = self.table_head[self.headers[i]].split(".")
                    if len(cell_info) > 2:
                        rating_symbol = cell_info[2]
                    rating_max = int(max(self.content, key=lambda x: int(x[i]))[i])
                    rating_percent = int(int(user_line[i]) / rating_max * 100)
                    field = self.raiting_view(width_cells[i] - len(str(user_line[i])) - self.padding, rating_percent,
                                              int(user_line[i]), rating_symbol)
                self.tab_str += f"{self.make_cell(field, width_columns[i], ' ', self.table_head[self.headers[i]], self.padding)}|"
            self.tab_str += f"\n{self.line}\n"

        return self

    def print(self):
        print(self.tab_str)
        return self

    def print_line(self, string, symbol):
        """
        Вывод строки в стиле заголовка
        :param string:
        :param symbol:
        :return:
        """

        if string:
            start_offset = ((len(self.line) - len(str(string)) - 2) // 2)
            end_offset = len(self.line) - len(str(string)) - start_offset - 2
            print(f"{symbol * start_offset} {string} {symbol * end_offset}")
        else:
            print(symbol * len(self.line))

    def update_field(self, col_name, row_num, new_value):
        self.content[row_num][self.headers.index(col_name)] = new_value
        self.build_tab()
        return self

    def set_content(self, content):
        self.content = content
        return self

    def del_line(self, col_name, value):
        for line in self.content:
            if line[self.headers.index(col_name)] == value:
                self.content.remove(line)
                self.build_tab()
                return True
        return False


class FakeDataBase:
    base_list = [
        {
            "id": "10",
            "firstname": "Николай",
            "lastname": "Меньшиков",
            "birthday": [27, 10, 1980],
            "gender": "Мужской",
            "login": "Niiik27",
            "password": "12345",
            "status": "user",
            "rating": 10,
        },
        {

            "firstname": "Денис",
            "lastname": "Кириллов",
            "birthday": [1, 6, 2001],
            "gender": "Мужской",
            "login": "Denis161",
            "password": "54321",
            "status": "user",
            "rating": 20,
        },
        {
            "firstname": "Екатерина",
            "lastname": "Исаева",
            "birthday": [25, 10, 2000],
            "gender": "Женский",
            "login": "Ekaterina25",
            "password": "11111",
            "status": "user",
            "rating": 30,
        },
        {
            "firstname": "Ольга",
            "lastname": "Владимирова",
            "birthday": [22, 11, 1999],
            "gender": "Женский",
            "login": "qqq",
            "password": "qqq",
            "status": "admin",
            "rating": 40,
        },
        {
            "id": "100500",
            "firstname": "Кирилл",
            "lastname": "Кириллов",
            "birthday": [17, 11, 2006],
            "gender": "Мужской",
            "login": "www",
            "password": "www",
            "status": "moderator",
            "rating": 50,
        },
    ]

    def __init__(self):
        self.base_list = FakeDataBase.base_list
        self.fill_id()

    @staticmethod
    def create_id(user_id_len=8):
        """
        В каких то старых домашках делал создатель ид. Теперь решил записатьего ввиде метода,
        но пока не решил - использовать или нет. Так что пусть будет. Дальше будет видно
        :param user_id_len:list
        :return:
        """
        new_id_user = ""
        id_symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        # id_symbols = "1234567890"  # упростил до цифр
        while True:
            for _ in range(user_id_len):
                symbol_index = random.randint(0, len(id_symbols) - 1)
                new_id_user += id_symbols[symbol_index]

            for user in FakeDataBase.base_list:
                if user.get('id') is not None and user.get('id') == new_id_user:
                    new_id_user = ""
                    break
            if len(new_id_user) != 0:
                break
        return new_id_user

    def fill_id(self):
        for item in self.base_list:
            # if item.get("id") is not None:
            item['id'] = self.create_id()

    def store_user_info(self, info):
        if info.get('id') is not None:  # id выдает сервер, так что если id нет, то это значит новый пользователь
            for rec in self.base_list:
                if rec['id'] == info['id']:
                    rec["firstname"] = info["firstname"]
                    rec["lastname"] = info["lastname"]
                    rec["birthday"] = info["birthday"]
                    rec["gender"] = info["gender"]
                    rec["login"] = info["login"]
                    rec["password"] = info["password"]
                    rec["status"] = info["status"]
                    rec["rating"] = info["rating"]
                    return info['id']
        info['id'] = self.create_id()
        self.base_list.append(info)
        return info['id']

    def delete_user_info_by_id(self, user_id):
        for rec in self.base_list:
            if rec['id'] == user_id:
                self.base_list.remove(rec)
                return True
        return False


class User:
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, user_list) -> None:
        self.user_id = user_id
        self.rating = rating
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        self.blocked = False
        self.status = "user"
        self.user_list: UsersList = user_list
        self.menu = Menu(["Редактировать профиль", "Удалиться", "Стать модератором",
                          "Стать админом", "Выход", "Вызвать ошибку"], "Меню пользователя")

    def get_str_status(self):
        if self.status == "user":
            return "пользователь"
        elif self.status == "moderator":
            return "модератор"
        elif self.status == "admin":
            return "админ"

    def get_user_info(self):
        return {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthday": self.birthday,
            "gender": self.gender,
            "login": self.login,
            "password": self.password,
            "rating": self.rating,
        }

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

        birth_date = self.birthday
        birth_year = birth_date[2]
        birth_month = birth_date[1]
        birth_day = birth_date[0]

        return int(current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day)))

    def to_table(self) -> list:
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

    def show_menu(self):
        return self.callback_menu(self.menu.show())

    def callback_menu(self, choice: int):
        if choice == 1:
            self.edit_me()
        elif choice == 2:
            self.delete_me()
        elif choice == 3:
            self.upgrade_to_moderator()
        elif choice == 4:
            self.upgrade_to_admin()
        elif choice == 5:
            self.exit_me()
        elif choice == 6:
            self.crash_me()

    def show(self):
        print(f"Данные пользователя {self.firstname}: ")
        print(f"id: {self.user_id}")
        print(f"Рейтинг:{self.rating}")
        print(f"Имя: {self.firstname}")
        print(f"фамилия: {self.lastname}")
        print(f"День рождения: {self.birthday[0]}.{self.birthday[1]}.{self.birthday[2]}")
        print(f"Возраст: {self.get_user_age()}")
        print(f"Пол: {self.gender}")
        print(f"Логин: {self.login}")
        print(f"Пароль: {self.password}")
        print(f"Статус: {self.status}")
        print(f"Состояние {'Заблокирован' if self.blocked else 'OK'}")

    @staticmethod
    def crash_me():
        return 1 / 0

    @staticmethod
    def exit_me():
        print("Пока")
        exit(0)

    def upgrade_to_admin(self):
        print("Еще не готово")

    def upgrade_to_moderator(self):
        print("Еще не готово")

    def delete_me(self):
        self.user_list.delete_user_by_id(self.user_id)
        self.user_list.table_view.print()

    def edit_me(self):
        menu = Menu(["Сменить имя", "Сменить фамилию", "Сменить логин",
                     "Сменить дату рождения", "Сменить пол", "Сменить пароль"],
                    "Меню редактирования данных пользователя")
        choice = menu.show()
        if choice == 1:
            self.edit_me()
        elif choice == 2:
            self.delete_me()
        elif choice == 3:
            self.upgrade_to_moderator()
        elif choice == 4:
            self.upgrade_to_admin()
        elif choice == 5:
            self.exit_me()
        elif choice == 6:
            self.crash_me()


class Moderator(User):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, user_list) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password, rating, user_list)
        self.status = "moderator"
        self.menu = Menu(["Заблокировать - укажите id пользователей через пробел",
                          "Разблокировать - укажите id пользователей через пробел", "Выход"], "Меню модератора")

    def blocking_users(self, user_ids):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.user_list.registered_users)):
                registered_user: User = self.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    if registered_user.status == "admin":
                        print("Вы не можете заблокировать админа")
                        continue
                    elif registered_user.status == "moderator":
                        print("Вы не можете заблокировать другого модератора. Обратитесь к администратору")
                        continue
                    registered_user.blocked = True
                    self.user_list.table_view.update_field("Состояние", j, "Заблокирован").print()
                    break

    def unblocking_users(self, user_ids):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.user_list.registered_users)):
                registered_user: User = self.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    registered_user.blocked = False
                    self.user_list.table_view.update_field("Состояние", j, "OK").print()
                    break

    def callback_menu(self, choice: int):
        if choice == 3:
            print("Досвидания")
            return False
        user_id = input("Введите id пользователей: ")
        if choice == 1:
            self.blocking_users(user_id)
        elif choice == 2:
            self.unblocking_users(user_id)

        return True


class Admin(Moderator):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, user_list) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password, rating, user_list)
        self.status = "admin"
        self.menu = Menu(["Заблокировать", "Разблокировать", "Добавить пользователя",
                          "Удалить пользователя", "Выход"], "Меню админа")

    @staticmethod
    def delete_user_list(user_list):
        user_list.clear()
        print("База данных пустая")

    def show_menu(self) -> int:
        return self.callback_menu(self.menu.show())

    def del_users(self, ids_str):
        print("Not ready")
        ids = ids_str.split(" ")
        # for id in ids:
        #     for base_user in base_list:
        #         if base_user["id"] == id:
        #             base_list.remove(base_user)
        #             break

    def add_users(self, user_id):
        print("Not ready")

    def callback_menu(self, choice: int):
        if choice == 5:
            print("Досвидания")
            return False
        self.user_list.show()
        user_id = input("Введите id пользователя: ")
        if choice == 1:
            self.blocking_users(user_id)
        elif choice == 2:
            self.unblocking_users(user_id)
        elif choice == 3:
            self.add_users(user_id)
        elif choice == 4:
            self.del_users(user_id)

        return True


class UsersList:
    def __init__(self):
        """
        В процессе написания кода стало неудобно хранить равнозначные массивы вне классов.
        По этому сделал обертку для registered_users, и добавил сопутствующих методов
        Так же теперь доступ к базе осуществляется через этот класс. На мой взгляд так будет понятней, когда мы
        сохраняем пользователя локально, и когда на сервере.
        При инициализации сразу запрашиваем список пользователей и приводим его к удобному формату

        Вообще обращение к базе данных теперь происходит через этот класс, так как требуется синхронизация полученных
        и хранимых локально данных

        Теперь у меня есть объект таблицы, и для реализации функции вывода данных в табличном формате больше не нужно
        придумывать метод вывода. Значит я могу создать внутри этого класса таблицу, для просмотра пользователей
        Возможно в дальнейшем она перекочует в менеджер, что бы класс не зависел от внезапно придуманных рюшечек.
        Пока не определился в этом вопросе потому что считаю допустимым иметь этому классу метод show()
        По скольку объем данных большой, то его нужно видеть максимально комфортно, не думая о том как это сделать
        А вот если потребуются элементы GUI то их уже делать отдельно

        Похоже пока писал комент - определился - таблице здесь быть.
        Хотелось бы сделать меню, но оно зависит от прав пользователя. Значит меню реализовывать в них
        """
        self.registered_users = []
        self.db = FakeDataBase()
        self.create_user_list(self.db.base_list)
        self.table_view = TableView(
            {"№": "center", "id": "left", "Имя": "left", "Пол": "center", "Логин": "left", "День рождения": "center",
             "Возраст": "rating.15.*", "Статус": "center", "Состояние": "center", "Пароль": "right",
             "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")

    def create_user_list(self, base_list):
        """
        Раньше это была автоматизация создания тестового списка пользователей, а теперь похоже рабочий метод.
        Тестовый список - теперь на стороне базы данных
        """

        for i in range(len(base_list)):
            if base_list[i]["status"] == "user":
                self.registered_users.append(User(
                    user_id=base_list[i]["id"],
                    firstname=base_list[i]["firstname"],
                    lastname=base_list[i]["lastname"],
                    birthday=base_list[i]["birthday"],
                    gender=base_list[i]["gender"],
                    login=base_list[i]["login"],
                    password=base_list[i]["password"],
                    rating=base_list[i]["rating"],
                    user_list=self,
                ))
            elif base_list[i]["status"] == "admin":
                self.registered_users.append(Admin(
                    user_id=base_list[i]["id"],
                    firstname=base_list[i]["firstname"],
                    lastname=base_list[i]["lastname"],
                    birthday=base_list[i]["birthday"],
                    gender=base_list[i]["gender"],
                    login=base_list[i]["login"],
                    password=base_list[i]["password"],
                    rating=base_list[i]["rating"],
                    user_list=self,
                ))
            elif base_list[i]["status"] == "moderator":
                self.registered_users.append(Moderator(
                    user_id=base_list[i]["id"],
                    firstname=base_list[i]["firstname"],
                    lastname=base_list[i]["lastname"],
                    birthday=base_list[i]["birthday"],
                    gender=base_list[i]["gender"],
                    login=base_list[i]["login"],
                    password=base_list[i]["password"],
                    rating=base_list[i]["rating"],
                    user_list=self,
                ))

    def check_in(self):
        """
        Есть общее правило как пройти проверку и стать частью списка со своими правами. значит проверку нужно
        реализовать в этом классе
        :return:
        """
        try_count = 5
        while try_count:
            my_login = input("Введите Логин ")
            my_pass = input("Введите пароль ")
            for i in range(len(self.registered_users)):
                registered_user = self.registered_users[i]
                if my_login == registered_user.login and my_pass == registered_user.password:
                    return registered_user
            try_count -= 1
            print(f"Логин или пароль не верный, осталось {try_count} чтобы войти")
        print("Отказано в доступе")
        return None

    def check_login(self, my_login) -> bool:
        """
        Кто то с другого компа может успеть занять мой логин. По этому доступность логина проверяю по базе данных.
        А может быть вообще. Все вопросы нужно решать через базу, а то сейчас получается база делится секретной
        информацией
        :param my_login:
        :return:
        """
        while len(my_login) == 0:
            print("Поле не может быть пусто!")
            my_login = input("Введите Логин ")
        for user in self.db.base_list:
            if my_login == user["login"]:
                return True
        return False

    def check_pass(self, my_login) -> dict | None:
        if self.check_login(my_login):
            my_pass = input("Введите Пароль ")
            while len(my_pass) == 0:
                print("Поле не может быть пусто!")
                my_pass = input("Введите Пароль")

            for usr in self.registered_users:
                if usr["myLogin"] == my_login:
                    if my_pass == usr["myPass"]:
                        return usr
                    else:
                        return None
            return None

    def create_id(self, user_id_len=8):
        """
        В каких то старых домашках делал создатель ид. Теперь решил записатьего ввиде метода,
        но пока не решил - использовать или нет. Так что пусть будет. Дальше будет видно
        :param user_id_len:list
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

    def edit_user(self, menu):
        ...

    def show(self):
        user_table_fields = []
        for i in range(len(self.registered_users)):
            user: User = self.registered_users[i]
            line = user.to_table()
            line.insert(0, i + 1)
            user_table_fields.append(line)

        self.table_view.set_content(user_table_fields).build_tab().print()

    def delete_user_by_id(self, user_id):
        if self.db.delete_user_info_by_id(user_id):
            for user in self.registered_users:
                if user.user_id == user_id:
                    self.registered_users.remove(user)
                    self.table_view.del_line("id", user_id)
                    return True
            return False


class Registration:
    def __init__(self, manager):
        """
        Это класс регистрации
        """
        self.manager: Manager = manager
        self.new_user = None

    def reister_new_user(self):
        while True:
            new_user = User(
                user_id=None,
                firstname=self.input_field("имя"),
                lastname=self.input_field("фамилию"),
                birthday=self.input_birthday(),
                gender=self.input_gender(),
                login=self.input_login(),
                password=self.input_pass("Придумайте пароль: "),
                rating=0,
                user_list=self.manager.user_list,
            )
            new_user.show()

            if not input("Enter - Подтвердить "):
                new_user.user_id = self.manager.user_list.db.store_user_info(new_user.get_user_info())
                self.manager.user_list.registered_users.append(new_user)
                self.new_user = new_user
                return new_user
            else:
                print("Начните регистрацию заново ")

    @staticmethod
    def input_field(field_name) -> str:
        name = input(f"Введите {field_name} ")
        while len(name) == 0:
            print("Поле не может быть пусто!")
            name = input(f"Введите {field_name} ")
        return name

    @staticmethod
    def input_gender() -> str:
        gender = Registration.input_field("пол")
        gender = gender.lower()
        if gender.startswith("м") or gender.startswith("m") or gender.startswith("v") or gender.startswith(
                "ь") or gender.startswith("1"):
            return "Мужской"
        elif gender.startswith("ж") or gender.startswith("w") or gender.startswith(";") or gender.startswith("2"):
            return "Женский"

    @staticmethod
    def input_birthday() -> list:
        birthday = Registration.input_field("день рождения в формате ДД.ММ.ГГГГ")
        if not birthday:
            birthday = "01.01.1970"
            print("Дата рождения не указана. Назначена 01.01.1970")
        birthdate = []
        parse_num = ""

        current_date = date.today().timetuple()
        current_year = current_date.tm_year
        control_nums = [31, 12, current_year]

        d = 0
        for char in birthday:
            if char.isdigit():
                parse_num += char

            elif parse_num:
                if len(birthdate) == 3:
                    return birthdate
                num = int(parse_num)
                if num <= control_nums[d]:
                    birthdate.append(num)
                    d += 1
                else:
                    print("Введена некорректная дата")
                    return Registration.input_birthday()
                parse_num = ""
        if len(birthdate) == 3:
            return birthdate
        else:
            birthdate.append(int(parse_num))
            return birthdate

    def input_login(self) -> str:
        """
        Проверяем свободен ли логин и если да то возвращаем его. если нет, то принуждаем ввести другой логин
        :return:
        """
        while True:
            my_login = Registration.input_field("логин")
            if not self.manager.user_list.check_login(my_login):
                return my_login
            print("Такой логин уже занят. Придумайте другой")

    @staticmethod
    def input_pass(password_name=''):
        """
        В учебно- тестовых целях сделал подсказку для пароля. не знаю буду ли ее использовать.
        может не понадобится, а удалить забуду, и в коде она будет сбивать с толку
        :param password_name:
        :return:
        """
        password = Registration.input_field("пароль" if not password_name else f"пароль {password_name}")
        return password


class LogIn:
    """
    Это класс входа
    """

    def __init__(self, manager):
        self.manager: Manager = manager
        self.login = None
        self.password = None

    def log_in_account(self):
        user: User = self.manager.user_list.check_in()
        if user is not None:
            self.login = user.login
            self.password = user.password
        return user


class Manager:
    """
    А нужно ли передавать в менеджер столько объектов?
    Возможно нужно их создавать прям внутри менеджера. Ведь дальнейшее взаимодействие с ними предпологается
    исключительно через менеджер

    Пока что убрал параметрры что бы было несложно поработать через менеджер
    """

    def __init__(self):
        self.registration = Registration(self)
        self.log_in: LogIn = LogIn(self)
        self.user = None
        self.user_list = UsersList()
        self.menu = Menu(["Вход", "Регистрация"], "Войдите или зарегистрируйтесь")

    def show_start_menu(self):
        if self.menu.show() == 1:
            self.user = self.log_in.log_in_account()
        else:
            self.user = self.registration.reister_new_user()
        if self.user:
            self.show_users()
            self.user.show_menu()

    def show_users(self):
        self.user_list.show()


account_manager = Manager()
# print(account_manager.registration.input_birthday())
account_manager.show_start_menu()
