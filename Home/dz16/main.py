"""
Если навести мышь на метод, то вылазит подсказка с описанием. Очень удобно.
Увлекся созданием описаний и подсказок. Подсказки по типам упращают кодинг - после точки появляются нормальные подсказки
по функциям объекта
так что постараюсь их напихать везде где нужно, За одно посмотрю сколько требуется времени на такое оформление
"""


class RegistrationMenu:
    def __init__(self):
        self.registered_users = []
        self.table_head = ["id", "Имя", "Логин", "День рождения", "Возраст", "Статус", "Состояние", "Пароль"]
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
        blocked_user_list = []
        for i in range(len(self.registered_users)):
            user:User = self.registered_users[i]
            blocked_user_list.append(user.to_table())
        self.print_tab(self.table_head,blocked_user_list,"Таблица заблокированных пользователей")


    def make_cell(self, my_string: str, cell_len: int, symbol: str = " "):
        """
        Метод созает строку нужной длины, и вписывает в середину другую строку
        :param my_string:
        :param cell_len:
        :param symbol:
        :return:
        """
        start_offset = (cell_len - len(my_string)) // 2
        end_offset = cell_len - len(my_string) - start_offset
        return f"{symbol * start_offset}{my_string}{symbol * end_offset}"


    def print_tab(self, tab_head: list, content: list, tab_name: str = "", padding: int = 1):
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
        field_str = "|"
        line = "|"

        list_of_width_cells = []
        width_cells = []
        """
        Сначала измерим ячейки и соберем информацию о них в общий массив массивов
        затем из каждого массива выберем максимум. Это нужно что бы определить где рисовать вертикальные линии.
        Этот код можно было сделать проще, если бы ширина столбцов выбиралась на основе только лишь заголовков,
        но стремление к компактности и легкости восприятия - потребовали усложнений
        """
        for col_name in tab_head:
            width_cells.append(padding + len(col_name) + padding)
        list_of_width_cells.append(width_cells)
        for user_line in content:
            """
            На всякий случай увеличим количество ячеек в строке.
            Это защитит от ошибки индекса. Но такая ситуация не предполагается        
            """
            while len(user_line) < len(tab_head):
                user_line.append("")
            width_cells = []
            for i in range(len(user_line)):
                field: str = user_line[i]
                """ширина ячейки равна ширине записи плюс отступы по бокам"""
                width_cells.append(padding + len(field) + padding)
            list_of_width_cells.append(width_cells)
        """Здесь я хотел использовать функцию map, но что то не заладилось. Пришлось использовать генератор массива
            он выбырает из массива массивов массив с наибольшим значением в соответствующем поле, и берет этот максимум
            в итоге получается список ширин колонок
        """
        width_columns = [max(list_of_width_cells, key=lambda x: x[z])[z] for z in range(len(tab_head))]
        """Художественное оформление шапки таблицы. Тут все примитивно, основная достопримечательность - .center"""
        """Все таки заменил встроенный метод собственным, чтоб оставаться в рамках задания"""
        for i in width_columns:
            line += "-" * i + "|"

        for i in range(len(tab_head)):
            field: str = tab_head[i]
            # field_str += field.center(width_columns[i], " ") + "|"
            field_str += f"{self.make_cell(field,width_columns[i])}|"

        print()
        if tab_name:
            # print(f" {tab_name} ".center(len(line), "*"))
            print(self.make_cell(f" {tab_name} ",len(line),'*'))
        print("_" * len(line))
        print(line.replace("-", " "))  # Найти и понять суть метода очень просто, по этому использую его
        # print(line)
        print(field_str)
        print(line)
        """Только здесь мы добрались до отображения данных таблицы"""
        for user_line in content:
            field_str = "|"
            for i in range(len(tab_head)):
                field: str = user_line[i]
                # field_str += field.center(width_columns[i], " ") + "|"
                field_str += f"{self.make_cell(field, width_columns[i])}|"
            print(field_str)
            print(line)

#
# head = ["id", "Имя - Фаммлия", "Логин/Пароль", "Пол", "Дата рождения", "Заблокированность", "Статус", "Какое то поле"]
#
# user_line1 = ["12321", "Николай Меньшиков Валерьевич", "Niiik2700 - 12345", "Мужской", "27.10.1980", "Заблокирован",
#               "Пользователь"]
# user_line2 = ["321456546546546565465466646tttt", "Алексей Меньшиков", "Lex24 - 521", "Мужскойоеоей", "24.03.1980666",
#               "", "Модератор", "Fuck"]
# user_lines = [user_line1, user_line2, ]
# rm = RegistrationMenu()
# rm.print_tab(head, user_lines, "Cписок пользователей")
