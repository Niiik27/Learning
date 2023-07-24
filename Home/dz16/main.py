"""
mongodb
Случилась глобальная переделка - Сделал класс RegistrationMenu.
На данный момент он позволяет не просто вывести меню, но и является менеджером для работы с классами Users & Children
По этому список зарегистрированных пользователей переехал в него.
Основной список шаблона оставил на месте так как он имитирует внешние данные

Кроме того решил сделать табличный вывод списка пользователей - показалось не сложно. Основное решение придумалось в
классе - сделать метод дополняющий строку пробелами до необходимой длины - это позволит выводить строки в столбики.
Но по пути столкнулся с множественными непредвиденными проблемками, вариантами их решений и новыми идеями.
В итоге пришлось разработать отдельный класс для вывода таблиц. Так как функционал меню и таблицы стали сильно
переплетаться, а мне бы хотелось иметь универсальный инструмент на будущее. По этому пришлось разделить на два класса.
Теперь таблицей можно пользоваться как принтом, и можно ралзвивать ее функционал по мере необходимости
Для теста таблицы понадобились дополнительные поля, по этому пришлоь немного поменять User
метод create_user_list пока что является тестовым по тому не очень красив, и видимо таковым еще на долго останется.

Код менялся непрерывно, что то я комментировал, нв какой то момент бросил, так что в коде могут встретиться дубликаты
коментариев, или коментарии от перемещенного кода. По этому решил здесь описать суть проделанной работы.
Метод меню разрабатывал ранее. Здесь его только применил
"""
import json
import os
import random
from datetime import date


# from Home.dz16.main import RegistrationMenu
# rm = RegistrationMenu()
class Menu:
    """
    Слишком часто требуется меню. С ограничениями на ввод. Для этого нужен отдельный метод.
    Но оно нужно в разных контекстах, и тогда придется дублировать метод в разные классы.
    По этому создал класс для данного метода. За одно это позволит сразу сохранить поля меню, а не создавать
    под них отдельный массив.
    Для построения меню нужен списк пунктов меню. Так же можно передать заголовок меню
    """

    def __init__(self, menu_list: list, msg: str = ""):
        self.menu_list = menu_list
        self.msg = msg

    def show(self) -> int:
        """
        Метод строит меню на основе списка пунктов меню, и возвращает номенр выбранного пункта
        Так же он запрещает вводить не числовые данные, что гарантирует корректную работу меню
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

    def item(self, name_item) -> int:
        """
        метод возвращает номер пункта по его названию
        нужен для того что бы можно было оперативно добавлять новые пункты меню, и при обработке выбора не перестраивать
        обработчик выбора, и вообще не задумываться о правильном порядке
        :param name_item:
        :return:
        """
        for i in range(len(self.menu_list)):
            item = self.menu_list[i].lower()
            if item == name_item.lower():
                return i + 1
        return -1
        # return self.menu_list.index(name_item)


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
        Метод дополняет строку символами до нужной длины, что приводит к распечатке таких строк в столбик
        Символы добавляются согласно выбранному позиционированию текста
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
        Метод превращает число в n-количество указанных символов. На основе данных на сколько процентов должна быть
        заполнена строка.
        Возвращает строку вида xx ********** где xx - исходное число, **** - выбранные для отображения символы в
        рассчитанном количестве
        :param cell_width:
        :param fill_percent:
        :param original_value:
        :param symbol:
        :return:
        """
        len_digit = 3
        symbols_num = int((cell_width - len_digit) / 100 * int(fill_percent))
        rating_line = f"{self.make_cell(str(original_value), len_digit, ' ', 'left')} {symbol * symbols_num}"
        return self.make_cell(rating_line, cell_width, " ", 'left', 0)

    def build_tab(self):
        """
            Метов строит таблицу из шапки и данных для дальнейшего вывода.
            возвращяет свой инстанс. Так удобнее вызывать принт. В целом удалось сделать задуманное, и больше нет
            желания как то менять код. Хоть он и самый сложный в этом классе - оставлю его без комментариев, так как он
            идет в дополнение к заданию, а в дальнейшем может пригодиться как самодостаточный элемент для просмотра
            данных, и уже не важно будет, что там под капотом. А лишние комментарии только мешали отладить код.
            Основная идея в том, что при изменении полей таблицы может поменяться ширина колонки, по этому нужно сначала
            все просчитать,а в нужный момент вызвать принт, а что бы принт можно было вызвать сразу после
            просчета - через точку - возвращается self
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
        """
        Распечатка подготовленой ранее таблицы
        :return:
        """
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
        """
        Обновление поля в заданной колонке в указанной строке новым значением
        :param col_name:
        :param row_num:
        :param new_value:
        :return:
        """
        self.content[row_num][self.headers.index(col_name)] = new_value
        self.build_tab()
        return self

    def set_content(self, content):
        """
        Установка тела таблицы
        :param content:
        :return:
        """
        self.content = content
        return self

    def del_line(self, col_name, value):
        """
        Удаляет строку из таблицы по значению поля в заданном столбце. Типа удаление записи по id.
        Но только по любым параметрам
        :param col_name:
        :param value:
        :return:
        """
        for line in self.content:
            if line[self.headers.index(col_name)] == value:
                self.content.remove(line)
                self.build_tab()
                return True
        return False

    def update_line(self, col_name, row_item, new_line):
        """
        Обновление всей строки по названию колонки и значению поля
        :param col_name:
        :param row_item:
        :param new_line:
        :return:
        """
        for i in range(len(self.content)):
            line = self.content[i]
            if line[self.headers.index(col_name)] == row_item:
                new_line.insert(0, i)
                self.content[i] = new_line
                self.build_tab()
                break
        return self

    def get_num_line(self, col_name, row_item):
        """
        Поиск номера строки по названию колонки из начению поля
        :param col_name:
        :param row_item:
        :return:
        """
        for i in range(len(self.content)):
            line = self.content[i]
            if line[self.headers.index(col_name)] == row_item:
                return i

    def clear(self):
        self.content.clear()


class FakeDataBase:
    """
    В конечном итоге пришел к выводу, что требуется какой то имитатор базы данных, доступ к которому будет
    целой историей с правильной последовательностью действий.
    В ней будут храниться данные пользователей в своем формате
    Класс имеет заводской массив пользователей, что бы не приходилось с нуля создавать список для тестов
    Все сохранения производятся в json на диск, а после сохранения информация считывается заново, что бы обновить
    локольный список пользователей согласно тому что храниться в базе
    """
    default_base_list = [
        {
            "id": "10",
            "firstname": "Николай",
            "lastname": "Меньшиков",
            "birthday": [27, 10, 1980],
            "gender": "Мужской",
            "login": "Niiik27",
            "password": "12345",
            "status": "user",
            "blocked": False,
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
            "blocked": False,
            "rating": 20,
        },
        {
            "firstname": "Екатерина",
            "lastname": "Исаева",
            "birthday": [25, 10, 2000],
            "gender": "Женский",
            "login": "eee",
            "password": "eee",
            "status": "user",
            "blocked": False,
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
            "blocked": False,
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
            "blocked": False,
            "rating": 50,
        },
    ]

    def __init__(self):
        """
        При инициализации происходит чтение данных либо с диска либо с шаблона
        """
        self.base_name = "db_users.json"
        if os.path.exists(self.base_name):
            file = open(self.base_name, "r", encoding="utf-8")
            base_list = file.read()
            self.base_list = json.loads(base_list)
            file.close()
        else:
            self.base_list = FakeDataBase.default_base_list

        # fileR2 = open('base.json', "r", encoding="utf-8")

        # primer = '[{"first_name":"Denis","age":22},{"first_name":"Masha","age":18}]'

        # base_list_read = fileR2.read()
        # print(base_list_read)
        # new_base = json.loads(base_list_read)
        # new_base_json = json.dumps(new_base, ensure_ascii=False)
        # print(new_base_json)
        #
        # fileR2.close()

        self.fill_id()

    def create_id(self, user_id_len=8):
        """
        Создает случайный id в строковам виде из буквенных и цифровых символов
        При создании проверяется уникальность id
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

            for user in self.base_list:
                if user.get('id') is not None and user.get('id') == new_id_user:
                    new_id_user = ""
                    break
            if len(new_id_user) != 0:
                break
        return new_id_user

    def fill_id(self):
        for item in self.base_list:
            if item.get("id") is None:
                item['id'] = self.create_id()

    def set_new_info(self, info):
        """
        Добавляет новую информацию для сохранения
        :param info:
        :return: id
        """
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
                    rec["blocked"] = info["blocked"]
                    rec["rating"] = info["rating"]
        else:
            info['id'] = self.create_id()
            self.base_list.append(info)
        # Единственное место где можно получить достоверный id нового пользователя находится здесь
        # Либо придется перезагружать базу. По этому этот метод должен возвращать id.
        return info['id']

    # def store_user_info(self, info):
    #     """
    #     Сохраняет информацию на диск
    #     :param info:
    #     :return:
    #     """
    #     self.add_new_info(info)
    #
    #     if self.save_base_list():
    #         return info['id']
    #     else:
    #         return None

    def save_base_list(self):
        """
        Здесь сам процесс записи.
        После записи информация считывается заново, что гарантирует соответствие полученной и сохраненной информации
        :return:
        """
        status = False
        file = open(self.base_name, "w", encoding="utf-8")
        if file:
            new_base_json = json.dumps(self.base_list, ensure_ascii=False)
            file.write(new_base_json)
            file.close()
            status = True
        if file:
            file = open(self.base_name, "r", encoding="utf-8")
            self.base_list = json.loads(file.read())
            file.close()
            status = True
        return status

    def delete_user_info_by_id(self, user_id):
        for rec in self.base_list:
            if rec['id'] == user_id:
                self.base_list.remove(rec)
                self.save_base_list()
                return True
        return False

    def reset_db(self):
        if os.path.exists(self.base_name):
            os.remove(self.base_name)
            self.base_list = FakeDataBase.default_base_list
            self.fill_id()
            self.save_base_list()


class User:
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, blocked,
                 manager) -> None:
        self.user_id = user_id
        self.rating = rating
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        self.blocked = blocked
        self.status = "user"
        self.manager: Manager = manager
        self.menu = Menu(["Редактировать профиль", "Удалиться", "Выход"], "Меню пользователя")

    def get_str_status(self):
        if self.status == "user":
            return "пользователь"
        elif self.status == "moderator":
            return "модератор"
        elif self.status == "admin":
            return "админ"

    def get_user_info(self):
        return {
            "id": self.user_id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "birthday": self.birthday,
            "gender": self.gender,
            "login": self.login,
            "password": self.password,
            "status": self.status,
            "blocked": self.blocked,
            "rating": self.rating,
        }

    def get_str_gender(self):
        if self.gender.lower() == "мужской":
            return "\u2642"
        elif self.gender.lower() == "женский":
            return "\u2640"

    def update_firstname(self):
        self.firstname = input(f"{self.firstname} {self.lastname} введите новое имя: ")

    def update_lastname(self):
        self.lastname = input(f"{self.firstname} {self.lastname} введите новую фамилию: ")

    def update_birthday(self):
        print(f"Прежняя дата рождения: {self.birthday[0]}.{self.birthday[1]}.{self.birthday[2]}")
        self.birthday = Registration.input_birthday()

    def update_gender(self):
        print(f"Прежний пол: {self.gender}")
        self.gender = Registration.input_gender()
        print(f"Выбран {self.gender} пол")

    def update_login(self):
        print(f"Прежний логин: {self.login}")
        self.login = self.manager.registration.input_login()
        print(f"Выбран {self.gender} пол")

    def update_password(self):
        print(f"Прежний пароль: {self.password}")
        old_password = ""
        while True:
            old_password = Registration.input_field("старый пароль")
            if old_password != self.password or old_password == "":
                print("Пароль не верный")
            else:
                break

        self.password = Registration.input_field("новый пароль")

    def get_user_age(self):
        """
        Для подсчета возраста воспользовался какой то библиотекой, которая выдает всякие даты в непонятном виде
        по этому пришлось их расшифровать
        :return:
        """
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
        """
        Метод выдает список полей строки таблицы. По этому потребуется его подстройка, если шапка таблицы изменится
        :return:
        """
        return [
            str(self.user_id),
            f"{self.firstname} {self.lastname}",
            self.get_str_gender(),
            self.login,
            f"{str(self.birthday[0]).rjust(2, '0')}.{str(self.birthday[1]).rjust(2, '0')}.{str(self.birthday[2]).rjust(4, '0')}",
            str(self.get_user_age()),
            self.status,
            f"{'Заблокирован' if self.blocked else 'ОК'}",
            self.password,
            self.rating
        ]

    def show_menu(self):
        """
        Показывает меню пользователя
        :return:
        """
        choice = 0
        while choice != self.menu.item("Выход") or choice != self.menu.item("Удалиться") or \
                choice != self.menu.item("Передать права администратора"):
            choice = self.menu.show()
            self.callback_menu(choice)

    def callback_menu(self, choice: int):
        """
        Обработка выбора меню
        :param choice:
        :return:
        """
        if choice == self.menu.item("Редактировать профиль"):
            self.edit_me()
        elif choice == self.menu.item("Удалиться"):
            self.delete_me()
        elif choice == self.menu.item("Выход"):
            self.exit_me()

    def show(self):
        """
        Показывает данные пользователя - для итоговой сверки перед дальнейшими действиями
        :return:
        """
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

    def exit_me(self):
        """
        Набор действий при выходе из программы
        :return:
        """
        self.manager.user_list.update_user_info(self)
        self.manager.user_list.create_user_list()
        self.manager.user_list.show()
        print("Пока")

    def delete_me(self):
        self.manager.user_list.delete_user_by_id(self.user_id)
        self.manager.user_list.show()
        self.manager.show_start_menu()

    def edit_me(self):
        """
        Локальное меню редактирования параметров пользователя
        :return:
        """
        menu = Menu(["Сменить имя", "Сменить фамилию", "Сменить логин",
                     "Сменить дату рождения", "Сменить пол", "Сменить пароль", "Завершить"],
                    "Меню редактирования данных пользователя")
        choice = 0
        while choice != menu.item("Завершить"):
            choice = menu.show()
            if choice == menu.item("Сменить имя"):
                self.update_firstname()
            elif choice == menu.item("Сменить фамилию"):
                self.update_lastname()
            elif choice == menu.item("Сменить логин"):
                self.update_login()
            elif choice == menu.item("Сменить дату рождения"):
                self.update_birthday()
            elif choice == menu.item("Сменить пол"):
                self.update_gender()
            elif choice == menu.item("Сменить пароль"):
                self.update_password()
        self.manager.user_list.table_view.update_line("id", self.user_id, self.to_table()).print()


class Moderator(User):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, blocked,
                 manager) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password, rating, blocked, manager)
        self.status = "moderator"
        self.menu = Menu(["Заблокировать - укажите id пользователей через пробел",
                          "Разблокировать - укажите id пользователей через пробел",
                          "Редактировать", "Удалиться", "Сбросить базу данных",
                          "Выход"], "Меню модератора")

    def blocking_users(self, user_ids):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.manager.user_list.registered_users)):
                registered_user: User = self.manager.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    if registered_user.status == "admin":
                        print("Вы не можете заблокировать админа")
                        continue
                    elif registered_user.status == "moderator":
                        print("Вы не можете заблокировать другого модератора. Обратитесь к администратору")
                        continue
                    registered_user.blocked = True
                    # self.manager.user_list.db.store_user_info(registered_user.get_user_info())
                    field = "Состояние"
                    self.manager.user_list.update_user_info(registered_user)
                    self.manager.user_list.show()
                    # self.manager.user_list.table_view.update_field("Состояние", j, "Заблокирован").print()
                    break

    def unblocking_users(self, user_ids):
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.manager.user_list.registered_users)):
                registered_user: User = self.manager.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    registered_user.blocked = False
                    # self.manager.user_list.db.store_user_info(registered_user.get_user_info())
                    field = "Состояние"
                    self.manager.user_list.update_user_info(registered_user)
                    self.manager.user_list.show()
                    # self.manager.user_list.table_view.update_field("Состояние", j, "OK").print()
                    break

    def callback_menu(self, choice: int):
        self.manager.user_list.show()
        if choice == self.menu.item("Заблокировать - укажите id пользователей через пробел"):
            user_id = input("Введите id пользователей: ")
            self.blocking_users(user_id)
        elif choice == self.menu.item("Разблокировать - укажите id пользователей через пробел"):
            user_id = input("Введите id пользователей: ")
            self.unblocking_users(user_id)
        elif choice == self.menu.item("Редактировать"):
            self.edit_me()
        elif choice == self.menu.item("Удалиться"):
            self.delete_me()
        elif choice == self.menu.item("Сбросить базу данных"):
            # сделал для упрощения восстановления админа
            self.manager.user_list.db.reset_db()
            self.manager.user_list.create_user_list()
            exit(0)
        elif choice == self.menu.item("Выход"):
            self.exit_me()


class Admin(Moderator):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password, rating, blocked,
                 manager) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password, rating, blocked, manager)
        self.status = "admin"
        self.menu = Menu(["Заблокировать", "Разблокировать", "Сделать пользователя модератором",
                          "Сделать модератора простым пользователем", "Передать права администратора",
                          "Удалить пользователей", "Редактировать", "Удалиться", "Сбросить базу данных",
                          "Выход"], "Меню админа")

    @staticmethod
    def delete_user_list(user_list):
        user_list.clear()
        print("База данных пустая")

    def del_users(self, ids_str):
        ids = ids_str.split(" ")
        for user_id in ids:
            self.manager.user_list.delete_user_by_id(user_id)
            self.manager.user_list.table_view.del_line("id", user_id)

        self.manager.user_list.table_view.print()

    def transfer_admin(self, user_id):
        """
        Передача админских прав другому пользователю
        Нельзя просто локально поменять статус, так как при получении данных создаются разные объекты пользователей
        Для этого придется создать новую запись, сохранить ее на сервере, поучить оттуда новые данные,,
        и на их основе заново создать пользователей
        Пока что для этого требуется закончить сеанс. В дальнейшем может сделаю смену прав без завершения работы
        :param user_id:
        :return:
        """
        for i in range(len(self.manager.user_list.registered_users)):
            registered_user: User = self.manager.user_list.registered_users[i]
            if user_id == registered_user.user_id:
                new_admin = registered_user.get_user_info()
                new_admin["status"] = self.status
                self.manager.user_list.update_base(new_admin)
                ex_admin = self.get_user_info()
                ex_admin["status"] = "user"
                self.manager.user_list.update_base(ex_admin)
                self.manager.show_start_menu()
                # self.exit_me()

    def set_users_to_moderator(self, user_ids):
        """
        Тоже что и с админом - нужно сменить запись и получить ее заново
        :param user_ids:
        :return:
        """
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.manager.user_list.registered_users)):
                registered_user: User = self.manager.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    if registered_user.status == "admin":
                        print("Админ не может быть изменен")
                        continue
                    new_moder = registered_user.get_user_info()
                    new_moder["status"] = "moderator"
                    self.manager.user_list.update_base(new_moder)
                    self.manager.user_list.save_base()
                    self.manager.user_list.create_user_list()
                    self.manager.user_list.show()

                    break

    def moderators_to_user(self, user_ids):
        """
        Тоже что и с админом - нужно сменить запись и получить ее заново
        :param user_ids:
        :return:
        """
        user_list = user_ids.split(" ")
        for i in range(len(user_list)):
            blocked_id: str = user_list[i].strip()
            for j in range(len(self.manager.user_list.registered_users)):
                registered_user: User = self.manager.user_list.registered_users[j]
                if blocked_id == registered_user.user_id:
                    new_moder = registered_user.get_user_info()
                    new_moder["status"] = "user"
                    self.manager.user_list.update_base(new_moder)
                    self.manager.user_list.save_base()
                    self.manager.user_list.create_user_list()
                    self.manager.user_list.show()
                    break

    def callback_menu(self, choice: int):
        self.manager.user_list.show()

        if choice == self.menu.item("Заблокировать"):
            user_id = input("Введите id пользователей для блокировки: ")
            self.blocking_users(user_id)
        elif choice == self.menu.item("Разблокировать"):
            user_id = input("Введите id пользователей для разблокировки: ")
            self.unblocking_users(user_id)
        elif choice == self.menu.item("Сделать пользователя модератором"):
            user_id = input("Введите id кандидатов в модераторы: ")
            self.set_users_to_moderator(user_id)
        elif choice == self.menu.item("Сделать модератора простым пользователем"):
            user_id = input("Введите id модераторов: ")
            self.moderators_to_user(user_id)
        elif choice == self.menu.item("Передать права администратора"):
            user_id = input("Введите id пользователя: ")
            self.transfer_admin(user_id)
            exit(0)
        elif choice == self.menu.item("Удалить пользователей"):
            user_id = input("Введите id удаляемых пользователей: ")
            self.del_users(user_id)
        elif choice == self.menu.item("Редактировать"):
            self.edit_me()
        elif choice == self.menu.item("Удалиться"):
            self.delete_me()
        elif choice == self.menu.item("Сбросить базу данных"):
            self.manager.user_list.db.reset_db()
            self.manager.user_list.create_user_list()
        elif choice == self.menu.item("Выход"):
            self.exit_me()


class UsersList:
    def __init__(self, manager):
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
        """
        self.manager = manager
        self.registered_users = []
        self.db = FakeDataBase()
        self.create_user_list()
        self.table_view = TableView(
            {"№": "center", "id": "left", "Имя": "left", "Пол": "center", "Логин": "left", "День рождения": "center",
             "Возраст": "rating.15.*", "Статус": "center", "Состояние": "center", "Пароль": "right",
             "Рейтинг": "rating"}, "Таблица зарегистрированных пользователей")

    def create_user_list(self):
        """
        Раньше это была автоматизация создания тестового списка пользователей, а теперь, похоже, рабочий метод.
        Тестовый список - теперь на стороне базы данных
        """
        self.registered_users.clear()
        for i in range(len(self.db.base_list)):
            if self.db.base_list[i]["status"] == "user":
                self.registered_users.append(User(
                    user_id=self.db.base_list[i]["id"],
                    firstname=self.db.base_list[i]["firstname"],
                    lastname=self.db.base_list[i]["lastname"],
                    birthday=self.db.base_list[i]["birthday"],
                    gender=self.db.base_list[i]["gender"],
                    login=self.db.base_list[i]["login"],
                    password=self.db.base_list[i]["password"],
                    rating=self.db.base_list[i]["rating"],
                    blocked=self.db.base_list[i]["blocked"],
                    manager=self.manager,
                ))
            elif self.db.base_list[i]["status"] == "admin":
                self.registered_users.append(Admin(
                    user_id=self.db.base_list[i]["id"],
                    firstname=self.db.base_list[i]["firstname"],
                    lastname=self.db.base_list[i]["lastname"],
                    birthday=self.db.base_list[i]["birthday"],
                    gender=self.db.base_list[i]["gender"],
                    login=self.db.base_list[i]["login"],
                    password=self.db.base_list[i]["password"],
                    rating=self.db.base_list[i]["rating"],
                    blocked=self.db.base_list[i]["blocked"],
                    manager=self.manager,
                ))
            elif self.db.base_list[i]["status"] == "moderator":
                self.registered_users.append(Moderator(
                    user_id=self.db.base_list[i]["id"],
                    firstname=self.db.base_list[i]["firstname"],
                    lastname=self.db.base_list[i]["lastname"],
                    birthday=self.db.base_list[i]["birthday"],
                    gender=self.db.base_list[i]["gender"],
                    login=self.db.base_list[i]["login"],
                    password=self.db.base_list[i]["password"],
                    rating=self.db.base_list[i]["rating"],
                    blocked=self.db.base_list[i]["blocked"],
                    manager=self.manager,
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
                    # self.table_view.del_line("id", user_id)
                    return True
            return False

    # def save_session(self, user: User):
    #
    #     self.db.add_new_info(user.get_user_info())
    #     self.db.save_base_list()
    #     return self.db.base_list

    def update_user_info(self, user: User):
        """
        метод обновляет локальный массив. и отправляет на сервер
        :param user:
        :return:
        """

        self.db.set_new_info(user.get_user_info())
        self.db.save_base_list()
        # self.registered_users.append(user)

    def update_base(self, record):
        """
        простое обновление локального массива без отправки на сервер
        Произойдет либо обновление данных пользователя, либо добавление данных нового пользователя
        id назначается на стороне базы данных, по этому метод должен возвращать id, так как если пользователь
        новый, то id появится только после занесения в базу
        :param record:
        :return:
        """
        return self.db.set_new_info(record)

    def save_base(self):
        """
        Сохраняет файл базы данных как есть
        :return:
        """
        self.db.save_base_list()
class Registration:
    def __init__(self, manager):
        """
        Это класс регистрации
        """
        self.manager: Manager = manager
        self.new_user = None

    def register_new_user(self):
        while True:
            new_user = User(
                user_id=None,
                firstname=self.input_field("имя"),
                lastname=self.input_field("фамилию"),
                birthday=self.input_birthday(),
                gender=self.input_gender(),
                login=self.input_login(),
                password=self.input_pass("Придумайте пароль: "),
                rating=random.randint(0, 100),
                blocked=False,
                manager=self.manager,
            )
            new_user.show()

            if not input("Enter - Подтвердить "):
                new_user.user_id = self.manager.user_list.update_base(new_user.get_user_info())
                self.manager.user_list.save_base()
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
            user.rating = random.randint(0, 100)
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
        self.user_list = UsersList(self)
        self.menu = Menu(["Вход", "Регистрация", "Показать базу данных пользователей", "Сброс базы данных"],
                         "Войдите или зарегистрируйтесь")

    def show_start_menu(self):
        choice = self.menu.show()
        if choice == self.menu.item("Вход"):
            self.user = self.log_in.log_in_account()
        elif choice == self.menu.item("Регистрация"):
            self.user = self.registration.register_new_user()
        elif choice == self.menu.item("Показать базу данных пользователей"):
            self.user_list.show()
            self.show_start_menu()
        elif choice == self.menu.item("Сброс базы данных"):
            self.user_list.db.reset_db()
            self.user_list.create_user_list()
            self.user_list.show()
            print("База данных сброшена")
            self.show_start_menu()

        if self.user:
            self.show_users()
            print(
                f"Добро пожаловать {self.get_user_alias(self.user.status).lower()} {self.user.firstname} {self.user.lastname}!")
            self.user.show_menu()

    def get_user_alias(self, user_name):
        if user_name.lower() == "admin":
            return "Администратор"
        elif user_name.lower() == "moderator":
            return "Модератор"
        elif user_name.lower() == "user":
            return "Пользователь"

    def show_users(self):
        self.user_list.show()


account_manager = Manager()
# print(account_manager.registration.input_birthday())
account_manager.show_start_menu()
