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






