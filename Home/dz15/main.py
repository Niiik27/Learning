"""
    С помощью классов в python создать ПК порядок запуска
    1. Блок питания
    2. Мат плата
    3. Процессор
    4. Оперативная память
    5. Видеокарта
    6. Постоянная память (SSD HDD m2.ssd)
"""
"""
Здесь основная задумка в том что все элеметы = электроприборы, и что бы не писать в каждом вкл выкл - 
сделал для них родительский класс электроприбора. Получилось возможно не очень красиво и не индивидуально,
зато универсально и еденообразно
Комментарии внутри кода отсутствуют так как особо нет функционала, а по названию и наследованию объектов и так понятно
что есть что
"""
from time import sleep

delay = .2


class Electrical:
    def __init__(self, name):
        self.power_on = False
        self.name = name

    def turn_on(self, message):
        self.power_on = True
        print(f"Устройство: {self.name} ({message})", end=" ")
        sleep(delay)

    def turn_off(self, message=""):
        self.power_on = False
        print(f"Устройство: {self.name} ({message})")
        sleep(delay)

    def check_power(self):
        print(f"Состояние: {'вкл.' if self.power_on else 'выкл.'}")
        return self.power_on


class Power(Electrical):
    def __init__(self, power):
        super().__init__("Блок питания")
        self.power = power
        self.turn_on("600W")
        self.check_power()


class Cpu(Electrical):
    def __init__(self, name):
        super().__init__("Центральный процессор")
        self.turn_on(name)
        sleep(delay)


class Ram(Electrical):
    def __init__(self, capasity, speed):
        super().__init__("Оперативная память")
        self.capasity = capasity
        self.turn_on(f"{self.capasity} {speed}")
        sleep(delay)


class Gpu(Electrical):
    def __init__(self, generation):
        super().__init__("Видеокарта")
        self.generation = generation
        self.turn_on(self.generation)

    sleep(delay)


class Rom(Electrical):
    def __init__(self, capacity, speed, name):
        super().__init__("Жесткий диск")
        self.capacity = capacity
        self.turn_on(f"{name} {self.capacity}MB {speed}")
        # print(f"Диск {self.capacity}MB {speed}:", end =" ")
        sleep(delay)


class RomSsdM2(Rom):
    def __init__(self, capasity):
        super().__init__(capasity, "superfast", "C:\>")
        self.form = "m2"

        # print("C:\> Рабочий диск подключен")
        sleep(delay)

    def load_sistem(self):
        print("C:\> загружается система")
        for i in range(20):
            print("*", end="")
            sleep(.3)
        print("*", end="\n")
        print("Hello Windows!")


class RomSsd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity, "fast", "D:\>")
        self.form = "2.5i"
        # print("D:\> Рабочий диск подключен")
        sleep(delay)


class RomHdd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity, "middle", "E:\>")
        self.form = "3.5i"
        # print("E:\> Архивный диск подключен")
        sleep(delay)


class Motherboard(Electrical):
    def __init__(self):
        super().__init__("Материнская плата")
        self.name = "Asus"
        self.turn_on("Professional 9000")
        self.check_power()
        sleep(delay)

        self.cpu = Cpu("Intel i7 6700")
        self.cpu.check_power()
        self.ram = Ram("32гб", "DDR4")
        self.ram.check_power()
        self.gpu = Gpu("Nvidia 960")
        self.gpu.check_power()
        self.sys_hdd = RomSsdM2(256)
        self.sys_hdd.check_power()
        self.work_hdd = RomSsd(256)
        self.work_hdd.check_power()
        self.base_hdd = RomHdd(1024)
        self.base_hdd.check_power()

    def switch_off(self):
        self.base_hdd.turn_off("E:\> Архивный диск")
        self.work_hdd.turn_off("D:\> Рабочий диск")
        self.sys_hdd.turn_off("С:\> System")
        self.gpu.turn_off("Nvidia 960")
        self.ram.turn_off("32гб DDR4")
        self.cpu.turn_off("Intel i7 6700")
        self.turn_off("Professional 9000")

        sleep(delay)


class SystemBlock:
    def __init__(self):
        while True:
            if not (len(input("Включить компьютер?"))):
                break
        self.power = Power(220)
        self.power.check_power()

    def switch_on(self):
        if self.power.power_on:
            self.motherboard = Motherboard()
            self.motherboard.sys_hdd.load_sistem()

    def switch_off(self):
        while True:
            if not (len(input("Выключите компьютер!"))):
                break
        self.motherboard.switch_off()


sb = SystemBlock()
sb.switch_on()
sb.switch_off()
