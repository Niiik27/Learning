"""
Сделать разблокировку пользователя
"""
import random
from datetime import date
from Home.dz16.main import RegistrationMenu
rm = RegistrationMenu()
table_head = ["id", "Имя", "Логин", "День рождения", "Возраст", "Статус", "Состояние", "Пароль"]
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

registered_users = [

]

class User:
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        self.status = "user"
        self.blocked = False

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

        return current_year - birth_year - ((current_month, current_day) < (birth_month, birth_day))

    def create_id(self, user_id_len, user_list):
        """
        В каких то старых домашках делал создатель ид. Теперь решил записатьего ввиде метода,
        но пока не решил - использовать или нет. Так что пусть будет. Дальше будет видно
        :param user_id_len:
        :param user_list:
        :return:
        """
        new_id_user = ""
        id_symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        while True:
            for _ in range(user_id_len):
                symbol_index = random.randint(0, len(id_symbols) - 1)
                new_id_user += id_symbols[symbol_index]

            for user in user_list:
                if user.user_id == new_id_user:
                    new_id_user = ""
                    break
            if len(new_id_user) != 0:
                break
        self.user_id = new_id_user


    def to_table(self):
        return [
                str(self.user_id),
                f"{self.firstname} {self.lastname}",
                self.login,
                self.birthday,
                str(self.get_user_age()),
                self.status,
                f"{'Заблокирован' if self.blocked else 'ОК'}",
                self.password
                ]


class Moderator(User):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password)
        self.status = "moderator"

    def blocking_users(self, user_list):
        # txt_user_list = ""
        blocked_user_list = []
        for i in range(len(user_list)):
            user:User = user_list[i]
            blocked_user_list.append(user.to_table())
            # txt_user_list += f"id - {user.user_id}: ФИо: {user.firstname} {user.lastname} {'Заблокирован' if user.blocked else ''} {user.status}\n"

            # txt_user_list += f"{i} - {user_list[i]['user_id']} {user_list[i]['firstname']} {user_list[i]['lastname']} {user_list[i]['blocked']} {user_list[i]['status']}\n"
        rm.print_tab(table_head,blocked_user_list,"Таблица заблокированных пользователей")
        # print(txt_user_list)
        input_user_id = int(input("Введите id пользователя для блокировки "))
        for i in range(len(user_list)):
            if self.status == "moderator":
                if input_user_id == i and user_list[i].status != "moderator" and user_list[i].status != "admin":
                    if user_list[i].blocked == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        user_list[i].blocked = True
                        print("Пользователь упешно заблокирован")
                        break
            elif self.status == "admin":
                if input_user_id == i:
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
        rm.print_tab(table_head, blocked_user_list, "Таблица заблокированных пользователей")

class Admin(Moderator):
    def __init__(self, user_id, firstname, lastname, birthday, gender, login, password) -> None:
        super().__init__(user_id, firstname, lastname, birthday, gender, login, password)
        self.status = "admin"
    
    def delete_user_list(self, user_list):
        user_list.clear()
        print("База данных пустая")

    def create_user_list(self, array, user_list):
        for i in range(len(array)):
            user_list.append( User(user_id = i,
                                firstname = array[i]["firstname"],
                                lastname = array[i]["lastname"],
                                birthday = array[i]["birthday"],
                                gender = array[i]["gender"],
                                login = array[i]["login"],
                                password = array[i]["password"]))
            
myAdmin = Admin(10, "admin", "admin", "01.01.1970", "Мужской", "admin", "admin")
    
myAdmin.create_user_list(base_list,registered_users)          
print(myAdmin.blocking_users(registered_users))


    #         {
    #     "firstname": "Екатерина",
    #     "lastname": "Исаева",
    #     "birthday": "25.10.2000",
    #     "gender": "Женский",
    #     "login": "Ekaterina25",
    #     "password": "11111",
    # },