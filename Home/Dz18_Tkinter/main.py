from tkinter import Tk, Label, Button, Entry, Text, Event, END
"""
Тема объемная. По этому поставил себе основную задачу - визуализация вывода и реагирование на нажатие кнопок
Думаю для начала пойдет, если позволит время - доработаю компановку
"""

class MainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.className='Интерфейс приложения на tkinter'
        self.geometry("600x480")

        self.label = Label(
            text="Так можно будет выводить какой нибудь текст",
            foreground="red", background="yellow", width=50, height=2
        )

        self.button = Button(
            text="Это кнопка для передачи из текста из однострочного поля ввода в лейбл",
            width=70,
            height=1,
            bg="gray",
            fg="yellow",

        )
        self.button2 = Button(
            text="Это кнопка для передачи текста из многострочного поля ввода в лейбл",
            width=70,
            height=1,
            bg="gray",
            fg="yellow",

        )
        self.button.bind("<Button-1>", self.callbak)
        self.button2.bind("<Button-1>", self.callbak)

        self.button3 = Button(
            text="Кнопка №3 - отобразит в лейбле свой номер при помощи команды",
            width=70,
            height=1,
            bg="gray",
            fg="yellow",
            command= lambda x=3:self.btn_command(3)
        )
        self.button4 = Button(
            text="Кнопка №4 - тоже отобразит свой номер",
            width=70,
            height=1,
            bg="gray",
            fg="yellow",
            command=lambda x=3:self.btn_command(4)
        )

        self.entry = Entry(fg="blue", bg="ivory2", width=50)

        self.txt = Text(fg="blue", bg="ivory2", width=50, height = 4)

        self.label.pack()

        self.entry.pack()

        self.txt.pack()
        self.button.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.mainloop()


    def callbak(self, event:Event):
        """
        Это отклик на кнопку, тут принты по исследованию кнопки - не стал удалять,
        так как это часть подхода к изучению.
        Здесь реализовал колбек через id кнопок
        :param event:
        :return:
        """
        event.widget:Button
        print(type(event))
        print(dir(event.widget))


        print(event.type)
        print(event.num)
        print(self.entry.get())


        if event.widget.winfo_id() == self.button.winfo_id():
            self.label.config(text=self.entry.get())
        elif event.widget.winfo_id() == self.button2.winfo_id():
            self.label.config(text=self.txt.get("1.0",END))

    def btn_command(self, param):
        self.label.config(text=f"Нажата кнопка номер {param}")
        if param == 3:
            self.label.config(background="Red")
            self.label.config(foreground="Blue")
        elif param == 4:
            self.label.config(background="Green")
            self.label.config(foreground="Blue")


if __name__ == '__main__':
    # Хоть пока только элементы tk, но уже можно запускать как приложение
    window = MainWindow()
