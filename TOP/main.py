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
class Utils:
    """
      Все таки нужен отдельный класс для общих функций.
      Можно было бы сделать класс меню, но пока что там просматривается только один метод
      с названием создать меню, объект меню тоже назывался бы меню. Получается что бы создать меню
      нужно трижды это произнести) Заклинание какое то.
      """

    @staticmethod
    def show_menu(menu_list: list, msg: str = "") -> int:
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

        Вспомнил - были вылеты из-за того что нельзя было создать меню.
        Эта проблема возникла из-за того что я решил отказаться от дублирования методов в разных классах.
        Вообще в соответствии модели вид-модель-контроллер - меню это элемент вида, и тебует отдельного класса.
        Проблема в том что пока там будет только один метод и тот статичный. Для этого было бы достаточно просто
        функции, но она может потеряться. меню могло бы хорошо встроиться в таблицу, как в часть вида, но там могут
        произойти какие нибудь нестыковки, что приведет к громоздкости
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

    def raiting_view(self, cell_width: int, fill_percent: int, original_value: int, symbol: str = "\u2588"):
        len_digit = 3
        symbols_num = int((cell_width - len_digit) / 100 * int(fill_percent))
        raiting_line = f"{self.make_cell(str(original_value), len_digit, ' ', 'left')} {symbol * symbols_num}"
        return self.make_cell(raiting_line, cell_width, " ", 'left', 0)

    def build_tab(self, content: list):
        """
        Метов выводит таблицу данных.

        :param tab_head: list Массив заголовков столбцов
        :param content: list Массив массивав данных таблицы
        :param tab_name: str Название таблицы
        :param padding: int Размер полей вокруг текста в таблице

        :return: None
        """

        self.line: str = "|"
        self.width_columns = []

        list_of_width_cells = []
        width_cells = []
        """ Сначала возьмем размеры с головы - заголовков колонок"""
        for col_name in self.table_head:
            width_cells.append(self.padding + len(col_name) + self.padding)
        list_of_width_cells.append(width_cells)  # Сохраняем массив в общий массив для глолвы и тела

        """теперь нам нужно найти самые широкие поля в колонках тела таблицы"""
        for user_line in content:

            while len(user_line) < len(self.table_head):
                """Возможно где то нехватило данных для заполнения полей таблицы. Тогда нужно их дозаполнить до
                количества колонок а то будет ошибка индекса"""
                user_line.append("")
            width_cells = []

            for i in range(len(user_line)):
                cel_str = str(user_line[i])
                """ширина ячейки равна ширине записи плюс отступы по бокам"""
                if "rating" in self.table_head[self.headers[i]]:
                    """Ищем максимальное значение в столбце, что бы по нему строить все рейтинги"""
                    rating_max = int(max(content, key=lambda x: int(x[i]))[i])
                    rating_percent = int(int(user_line[i]) / rating_max * 100)
                    rating_len = self.rating_len
                    rating_symbol = self.rating_symbol
                    cell_info = self.table_head[self.headers[i]].split(".")
                    if len(cell_info) > 1:
                        rating_len = int(cell_info[1])
                    if len(cell_info) > 2:
                        rating_symbol = cell_info[2]

                    cel_str = self.raiting_view(rating_len, rating_percent, int(user_line[i]), rating_symbol)

                """Сделали для строки тела то же что и для шапки - собрали ширины каждой ячейки в строке"""
                width_cells.append(self.padding + len(cel_str) + self.padding)

            """сохранили в общий массив"""
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

        field_str = "|"

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

                    field = self.raiting_view(rating_len, rating_percent, int(user_line[i]), rating_symbol)

                field_str += f"{self.make_cell(field, self.width_columns[i], ' ', self.table_head[self.headers[i]], self.padding)}|"
            print(field_str)
            print(self.line)


class FakeDataBase:
    base_list = [
        {
            "id": "10",
            "firstname": "Николай",
            "lastname": "Меньшиков",
            "birthday": "27.10.1980",
            "gender": "Мужской",
            "login": "Niiik27",
            "password": "12345",
            "status": "admin",
        },
        {
            "id": "100500",
            "firstname": "Денис",
            "lastname": "Кириллов",
            "birthday": "01.06.2001",
            "gender": "Мужской",
            "login": "Denis161",
            "password": "54321",
            "status": "moderator",
        },
        {
            "firstname": "Екатерина",
            "lastname": "Исаева",
            "birthday": "25.10.2000",
            "gender": "Женский",
            "login": "Ekaterina25",
            "password": "11111",
            "status": "user",
        },
        {
            "firstname": "Ольга",
            "lastname": "Владимирова",
            "birthday": "22.11.1999",
            "gender": "Женский",
            "login": "Olya22",
            "password": "22222",
            "status": "user",
        },
        {
            "firstname": "Кирилл",
            "lastname": "Кириллов",
            "birthday": "17.11.2006",
            "gender": "Мужской",
            "login": "Kirillooo",
            "password": "55555",
            "status": "user",
        },
    ]

    def __init__(self):
        self.base_list = FakeDataBase.base_list
        self.fill_id()

    @staticmethod
    def create_id(registered_users, user_id_len=8):
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

            for user in registered_users:
                if user.get('id') is not None and user.get('id') == new_id_user:
                    new_id_user = ""
                    break
            if len(new_id_user) != 0:
                break
        return new_id_user

    def fill_id(self):
        for item in self.base_list:
            if item.get("id") is not None:
                item['id'] = self.create_id(self.base_list)

    def store_user_info(self, info):
        for rec in self.base_list:
            if rec['id'] == info['id']:
                rec["firstname"] = info["firstname"]
                rec["lastname"] = info["lastname"]
                rec["birthday"] = info["birthday"]
                rec["gender"] = info["gender"]
                rec["login"] = info["login"]
                rec["password"] = info["password"]
                rec["status"] = info["status"]
                return
        self.base_list.append(info)

    def delete_user_info_by_id(self, user_id):
        for rec in self.base_list:
            if rec['id'] == user_id:
                self.base_list.remove(rec)
                return True
        return False


class UsersList:
    def __init__(self, base_list):
        """
        В процессе написания кода возникло предположение, что registered_users Должен стать частью RegistrationMenu
        Но позже возникло обратное предположение - что он должен быть сам по себе
        Но мне не нравится что он не в классе. Прямой доступ сбивает с толку.
        По этому решил его обернуть в собственныц класс.
        Сюда же перекочевали метод по его заполнению, и проверке логинов и паролей
        В общем будет все что необходимо для корректного доступа к списку пользователей и получения пользователя с
        определенным статусом
        """
        self.registered_users = []
        self.create_user_list(base_list)
        self.table_view = TableView(
            {"№": "center", "id": "left", "Имя": "left", "Пол": "center", "Логин": "left", "День рождения": "center",
             "Возраст": "rating.15.*", "Статус": "center", "Состояние": "center", "Пароль": "right",
             "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")

    def create_user_list(self, base_list):
        """
        Здесь заполняем список пользователей что бы было хоть что то, и не приходилось каждый раз создавать список
        По этому пришлось вклбчить в код детали таблицы
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
                    password=base_list[i]["password"]))
            elif base_list[i]["status"] == "admin":
                self.registered_users.append(Admin(
                    user_id=base_list[i]["id"],
                    firstname=base_list[i]["firstname"],
                    lastname=base_list[i]["lastname"],
                    birthday=base_list[i]["birthday"],
                    gender=base_list[i]["gender"],
                    login=base_list[i]["login"],
                    password=base_list[i]["password"]))
            elif base_list[i]["status"] == "moderator":
                self.registered_users.append(Moderator(
                    user_id=base_list[i]["id"],
                    firstname=base_list[i]["firstname"],
                    lastname=base_list[i]["lastname"],
                    birthday=base_list[i]["birthday"],
                    gender=base_list[i]["gender"],
                    login=base_list[i]["login"],
                    password=base_list[i]["password"]))





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

    def check_login(self, my_login) -> bool:
        while len(my_login) == 0:
            print("Поле не может быть пусто!")
            my_login = input("Введите Логин ")
        for user in self.registered_users:
            if my_login == user.login:
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

    def edit_user(self, menu):
        ...

    def show(self):
        self.line: str = "|"
        self.width_columns = None

        user_table_fields = []

        for i in range(len(self.registered_users)):
            user: User = self.registered_users[i]
            line = user.to_table()
            line.insert(0, i + 1)
            user_table_fields.append(line)

        self.table_view.build_tab(user_table_fields)
        self.table_view.print_tab(user_table_fields)


db = FakeDataBase()
uset_list = UsersList(db.base_list)


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
        return self.callback_menu(Utils.show_menu(["Редактировать профиль", "Удалиться", "Стать модератором",
                                                   "Стать админом", "Выход", "Вызвать ошибку"], "Меню пользователя"))

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

    def crash_me(self):
        return 1 / 0

    def exit_me(self):
        print("Пока")
        exit(0)

    def upgrade_to_admin(self):
        pass

    def upgrade_to_moderator(self):
        pass

    def delete_me(self):
        pass

    def edit_me(self):
        # return self.callback_menu(Utils.show_menu(["Сменить имя", "Сменить фамилию", "Сменить логин",
        #                           "Сменить дату рождения", "Сменить пол", "Сменить пароль"],
        #                          "Меню редактирования данных пользователя")+6)
        choice = self.callback_menu(Utils.show_menu(["Сменить имя", "Сменить фамилию", "Сменить логин",
                                                     "Сменить дату рождения", "Сменить пол", "Сменить пароль"],
                                                    "Меню редактирования данных пользователя"))
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
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password)
        self.status = "moderator"


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
                    menu.user_table_fields[i][menu.table_view.headers.index("Состояние")] = "Заблокирован"
                    break
        menu.table_view.build_tab(menu.user_table_fields)

    def unblocking_users(self, user_ids, menu):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for i in range(len(menu.registered_users)):
                registered_user: User = menu.registered_users[i]
                if blocked_id == registered_user.user_id:
                    registered_user.blocked = False
                    menu.user_table_fields[i][menu.table_view.headers.index("Состояние")] = "OK"
                    break
        menu.table_view.build_tab(menu.user_table_fields)

    def show_menu(self) -> int:
        return Utils.show_menu(["Заблокировать - укажите id пользователей через пробел",
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
        return self.callback_menu(Utils.show_menu(["Заблокировать", "Разблокировать", "Добавить пользователя",
                                                   "Удалить пользователя", "Выход"], "Меню админа"))

    def del_users(self, ids_str):
        ids = ids_str.split(" ")
        for id in ids:
            for base_user in base_list:
                if base_user["id"] == id:
                    base_list.remove(base_user)
                    break

    def callback_menu(self, choice: int):
        if choice == 5:
            print("Досвидания")
            return False
        regMenu.show_users()
        user_id = input("Введите id пользователя: ")
        if choice == 1:
            self.blocking_users(user_id, regMenu)
        elif choice == 2:
            self.unblocking_users(user_id, regMenu)
        elif choice == 3:
            self.blocking_users(user_id, regMenu)
        elif choice == 4:
            self.unblocking_users(user_id, regMenu)

        return True


class RegistrationMenu:
    def __init__(self):
        """
        Это класс регистрации
        """
        self.registered_users = []
        self.line: str = "|"
        self.width_columns = None

        self.table_view = TableView(
            {"№": "center", "id": "left", "Имя": "left", "Пол": "center", "Логин": "left", "День рождения": "center",
             "Возраст": "rating.15.*", "Статус": "center", "Состояние": "center", "Пароль": "right",
             "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")

        self.user_table_fields = []

    def show_menu(self):
        return self.callback_menu(Utils.show_menu(["Вход", "Регистрация"], "Войдите или зарегистрируйтесь"))

    def callback_menu(self, choice):
        if choice == 1:
            return regMenu.check_in()
        else:
            return regMenu.reister_new_user()

    def show_users(self):
        self.table_view.print_tab(self.user_table_fields)

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

    def input_field(self, field_name) -> str:
        name = input(f"Введите {field_name} ")
        while len(name) == 0:
            print("Поле не может быть пусто!")
            name = input(f"Введите {field_name} ")
        return name

    def input_gender(self) -> str:
        gender = self.input_field("пол")
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
            my_login = self.input_field("пол")
            if not self.check_login(my_login):
                return my_login
            print("Такой логин уже занят!")

    def input_pass(self, password_name=''):
        password = self.input_field("пароль" if not password_name else f"пароль {password_name}")
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
                self.user_table_fields.append(line)
                self.table_view.build_tab(self.user_table_fields)

                return new_user
            else:
                print("Начните регистрацию заново ")


class Manager():
    def __init__(self, reg, in_log, user_moder_admin, data_list):
        self.reg = reg
        self.in_log = in_log
        self.user_moder_admin = user_moder_admin
        self.data_list = data_list
        self.registered_users = []


class LoginMenu():
    """
    Это класс входа
    """

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def log_in_account(self):
        user: User = self.registered_users.check_in()
        if user is not None:
            self.login = user.login
            self.password = user.password


regMenu = RegistrationMenu()
regMenu.create_user_list()

print(regMenu.table_view.make_cell(
    " Тестовая строка из-за которой пришлось перелопатить и резделить таблицу на измерение и отрисовку ",
    len(regMenu.table_view.line), "|"))

print(regMenu.table_view.make_cell(" Показываю таблицу пользователей, что бы можно было выбрать логин/пароль для входа",
                                   len(regMenu.table_view.line), "|"))
regMenu.show_users()  # Придется сначала увидеть список пользователей что бы решить под кем входить

entered_user = regMenu.show_menu()
regMenu.show_users()

print()
print(f"Добро пожаловать {entered_user.get_str_status()} {entered_user.firstname} {entered_user.lastname}")

while entered_user.show_menu():
    regMenu.show_users()

my_reg = RegistrationMenu()
my_inlog = LoginMenu()
my_person_list = [User(), Moderator(), Admin()]
base = []
my_manager = Manager(my_reg, my_inlog, my_person_list, base)
