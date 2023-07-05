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
from abc import ABC, abstractmethod

delay = .2


class Electrical(ABC):
    """
    Это абстрактный класс, реализующий основное свойство любого эдектроприбора - включение/выключение
    """
    """
    В процессе написания кода мне понадобилась статическая переменная для учета общей нагрузки
    Можно было бы ее сделать частью блока питания, но тогда пришлось бы пробрасывать материнку до этого класса,
    что навязало бы конкретики абстрактному классу и привязало бы его к материнке.
    """
    __limit_power = 0  # Двойное подчеркивание должно придавать приватный статус, но не проверял
    __current_power = 0
    # Требуется пиватная переменная по этому даже если это не сработало, буду считать ее условно приватной
    @abstractmethod
    def __init__(self, name):
        """
        Для отображения состояния и названия прибора сделал соответствующие переменные
        название могло бы быть индивидуальным для каждого прибора, но прибор без названия - не прибор
        по этому название стоит хранить в суперклассе
        :param name:
        """
        self.power_on = False
        self.name = name

    def set_limit_power(self, power=None):
        """
        Потребовался вот такой вот костыль. Нужно задать лимит по нагрузке. Это будет делаться в классе БП
        но это возможно сделать из любого другого наследника. Хотелось бы бп наделить специалоьными правами
        """
        if power is not None and type(power) == Power and Electrical.__limit_power == 0:
            Electrical.__limit_power = power.power
            Electrical.__current_power = Electrical.__limit_power
            print(f"~Установлено ограничение по мощности {Electrical.__limit_power}W")
        else:
            if power is None:
                print("Что то несуществующее хочет изменить лимит")
            elif Electrical.__limit_power > 0:
                print(f"В процессе работы нельзя заменить блок питания.")
            else:
                print(f"Только блок питания может установить ограничение по потреблению мощности.")
    def take_power(self, percent):
        Electrical.__current_power -= Electrical.__limit_power * percent / 100
        if Electrical.__current_power <= 0:
            print(f"<Блок питания сдох. Осталось {max(Electrical.__current_power,0)}W>")#Причина лимита мощности в ограниченных возможностях блока питания
            # По этому класс хоть и абстрактный - можно сослаться на БП, тем более именно БП определяет этот лимит
            # А учет мощности ведется ради соответствия возможностям блока питания
            return False
        else:
            print(f"<Осталось {Electrical.__current_power}W мощности>")
            return True

    def turn_on(self, message):
        """
        Ради этого метода класс и создавался, на всякий случай дополнил его мессаджем, а то одного имени
        для выводв инфо может оказаться мало
        :param message:
        :return:
        """
        self.power_on = True

        if message:
            print(f"Устройство: {self.name} ({message})", end=" ")
        else:
            print(f"Устройство: {self.name} ", end=" ")
        sleep(delay)
        sleep(delay)

    def turn_off(self, message=""):
        """
        Ради этого метода класс и создавался, на всякий случай дополнил его мессаджем, а то одного имени
        для выводв инфо может оказаться мало
        :param message:
        :return:
        """
        self.power_on = False
        if message:
            print(f"Устройство: {self.name} ({message}) выключено")
        else:
            print(f"Устройство: {self.name} выключено")
        sleep(delay)

    def check_power(self):
        """
        Должен быть хоть какой то функционал.
        В зависимости от состояния прибора должны быть или нен быть какие то действия
        по этому пока сделал такой метод.
        Но возможно он не понадобится, так как его польза могла бы проявиться в многопоточном решении,
        а в данном случае все приборы будут включены при создании
        :return:
        """
        print(f"Состояние: {'вкл.' if self.power_on else 'выкл.'}")
        return self.power_on


class Power(Electrical):
    """
    "Это блок питания
    """

    def __init__(self, power):
        super().__init__("Блок питания")
        """
        Можно включить и после создания, но без питания нет никакого функционала, по этому включаю сразу
        """
        self.power = power
        self.capacity = 100
        self.turn_on(f"{power}W")
        self.check_power()
        self.set_limit_power(self)


class Cpu(Electrical):
    """
    "Это  центральный процессор
    """

    def __init__(self, name, self_power, motherboard):
        """
        Процессор, как и все остальные комплектующие, взаимосвязан с матереинкой по этому передаю указываю ее в параметр
        Идея в том что каждый прибор потребляет энергию, и если суммарное потребление
        будет больше чем дает блок питания - компьютер зависнет
        К этому и буду стремиться
        А все приборы связаны друг с другом через материнку
        :param name:
        :param motherboard:
        """
        """
        Первоначальная идея была в том что бы через материкскую плату добираться до БП и там уменьшать
        оставшуюся мощность. Но забирать энергию свойство любого электроприбора, по этому это свойство реализовал
        в классе электроприбора, а параметр motherboard сохранил, так как в дальнешем может возникнуть необходимость
        взаимодействия с другими компонентами материнской платы
        """
        super().__init__("Центральный процессор")
        self.motherboard = motherboard
        self.turn_on(name)
        if self.check_power() and self.take_power(self_power):
            sleep(delay)
        else:
            self.motherboard.switch_off("Блок питания не справился")


class Ram(Electrical):
    """
    Класс оперативки, пока ни чего интересного просто объект без функционала
    """
    def __init__(self, capasity, speed, self_power, motherboard):
        super().__init__("Оперативная память")
        self.motherboard = motherboard
        self.capasity = capasity
        self.turn_on(f"{self.capasity} {speed}")
        if self.check_power() and self.take_power(self_power):
            sleep(delay)
        else:
            self.motherboard.switch_off("Блок питания не справился")


class Gpu(Electrical):
    """
    Класс видеокарты, пока ни чего интересного просто объект без функционала
    """
    def __init__(self, generation, self_power, motherboard):
        super().__init__("Видеокарта")
        self.motherboard = motherboard
        self.generation = generation
        self.turn_on(self.generation)

        if self.check_power() and self.take_power(self_power):
            sleep(delay)
        else:
            self.motherboard.switch_off("Блок питания не справился")


class Rom(Electrical, ABC):
    """
    Абстрактный Класс жесткого диска, пока ни чего интересного просто объект без функционала
    просто выводит общую информацию в зависимости от детей
    """
    @abstractmethod
    def __init__(self, capacity, speed, name, self_power, motherboard):
        super().__init__("Жесткий диск")
        self.motherboard = motherboard
        self.capacity = capacity
        self.turn_on(f"{name} {self.capacity}MB {speed}")
        if self.check_power() and self.take_power(self_power):
            sleep(delay)
        else:
            self.motherboard.switch_off("Блок питания не справился")


class RomSsdM2(Rom):
    """
    Разновидность жесткого диска. Этот самый быстрый, и потому системный
    """
    def __init__(self, capasity, self_power, motherboard):
        super().__init__(capasity, "superfast", "C:\>", self_power, motherboard)
        self.form = "m2"


        sleep(delay)

    def load_sistem(self):
        print("C:\> загружается система")
        for i in range(20):
            print("*", end="")
            sleep(.3)
        print("*", end="\n")
        print("Hello Windows!")


class RomSsd(Rom):
    """
    Разновидность жесткого диска. Этот старый ссд - бывший системный, а ныне хранит файлы к которым нужно часто и
    быстро обращаться
    """
    def __init__(self, capacity, self_power, motherboard):
        super().__init__(capacity, "fast", "D:\>", self_power, motherboard)
        self.form = "2.5i"
        # print("D:\> Рабочий диск подключен")
        sleep(delay)


class RomHdd(Rom):
    """
    Разновидность жесткого диска. Любой диск боьшого объема, для хранения дистрибуивов, фото, и прочей редкой ерунды
    """
    def __init__(self, capacity, self_power, motherboard):
        super().__init__(capacity, "middle", "E:\>", self_power, motherboard)
        self.form = "3.5i"
        # print("E:\> Архивный диск подключен")
        sleep(delay)


class Flash(Rom):
    """
    Флешка - нужна для перегрузки блока питания
    """
    def __init__(self, capacity, self_power, motherboard):
        super().__init__(capacity, "low", "H:\>", self_power, motherboard)
        self.form = "USB"
        sleep(delay)


class Motherboard(Electrical):
    """
    Материнка - собрала в себе все устройства
    """
    def __init__(self, power):
        super().__init__("Материнская плата Asus")

        self.power = power

        """
        Возможны падения при загрузке компа, если не хватит мощности.
        Для этого определяю заранее переменные, что бы при аварийном выключении не орало, что нет такой переменной
        """
        self.cpu = None
        self.ram = None
        self.gpu = None
        self.sys_hdd = None
        self.work_hdd = None
        self.base_hdd = None

        # остальное должно работать только если питание включено, но пока не придумал как сделать ожидание включения
        # питания. По этому не будет условия проверки питания

        self.turn_on("Professional 9000")
        if self.check_power() and self.take_power(10):
            sleep(delay)
        else:
            self.switch_off("Блок питания не справился")
        self.cpu = Cpu("Intel i7 6700", 10, self)
        self.ram = Ram("32гб", "DDR4", 10,self)
        self.gpu = Gpu("Nvidia 960", 10,self)
        self.sys_hdd = RomSsdM2(256, 10,self)
        self.work_hdd = RomSsd(256, 10,self)
        self.base_hdd = RomHdd(1024, 10,self)


    def switch_off(self, reason):
        """
        По скольку теперь возможно аварийное выключение то было бы неплохо знать причину
        :param reason:
        :return:
        """
        if self.base_hdd:
            self.base_hdd.turn_off("E:\> Архивный диск")
        if self.work_hdd:
            self.work_hdd.turn_off("D:\> Рабочий диск")
        if self.sys_hdd:
            self.sys_hdd.turn_off("С:\> System")
        if self.gpu:
            self.gpu.turn_off("Nvidia 960")
        if self.ram:
            self.ram.turn_off("32гб DDR4")
        if self.cpu:
            self.cpu.turn_off("Intel i7 6700")
        self.turn_off("Professional 9000")
        self.power.power_on = False
        print(f"Компьютер выключен по причине: {reason}")
        sleep(delay)
        exit(0)


class SystemBlock:
    """
    Системный блок - нужен для организации процесса
    """
    def __init__(self):
        while True:
            if not (len(input("Что бы включить компьютер нажмите Enter"))):
                break



    def switch_on(self):
        self.power = Power(600)
        self.motherboard = Motherboard(self.power)
        self.motherboard.sys_hdd.load_sistem()

    def switch_off(self):
        while True:
            if not (len(input("Выключите компьютер!"))):
                break
        self.motherboard.switch_off("Пользователь сам выключил")

    def set_flash(self):
        return Flash("128гб USB 3.1",50,self.motherboard)

    def show_menu(self, menu_list, msg=""):
        """
        Менюшка из прошлых заданий. может быть статичной, и не в этом классе, но пока не важно
        :param menu_list:
        :param msg:
        :return:
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


sb = SystemBlock()
sb.switch_on()
if sb.show_menu(["Выключить","Вставить флешку"], "Что сделать дальше?") ==1:
    sb.switch_off()
else:
    sb.set_flash()
sb.switch_off()