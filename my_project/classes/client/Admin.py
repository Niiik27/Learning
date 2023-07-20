from my_project.classes.client.Moderator import Moderator


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