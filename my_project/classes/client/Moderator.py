from my_project.classes.client.User import User


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
        return Utils.show(["Заблокировать - укажите id пользователей через пробел",
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