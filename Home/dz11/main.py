"""
    С помощью классов в python создать ПК порядок запуска
    1. Блок питания
    2. Мат плата
    3. Процессор
    4. Оперативная память
    5. Видеокарта
    6. Постоянная память (SSD HDD m2.ssd)
"""
from time import sleep
class Power:
    def __init__(self, power):
        self.power = power
        print(f"Блок питания {self.power}V")
        self.power_on = False

    def turn_on(self):
        self.power_on = True
        print(f"Питание {self.power} вольт включено")
        sleep(.3)
        
class Motherboard:
    def __init__(self, name):
        self.name = name
        print(f"Материнская {self.name} press F1 to set BIOS")
        sleep(.3)

    def turn_off(self):
        print(f"Материнская {self.name} отключена")
        sleep(.3)


class Cpu:
    def __init__(self, name):
        self.name = name
        print(f"CPU {self.name} активирован")
        sleep(.3)

    def turn_off(self):
        print(f"CPU {self.name} отключен")
        sleep(.3)
        
        
class Ram:
    def __init__(self, capasity, speed):
        self.capasity = capasity
        print(f"ОЗУ {self.capasity} {speed} активирована")
        sleep(.3)


    def turn_off(self):
        print("ОЗУ отключена")
        sleep(.3)
        
        
class Gpu:
    def __init__(self, generation):
        self.generation = generation
        print(f"Графический процессор {self.generation} активирован")
    sleep(2)
    def turn_off(self):
        print(f"Графический процессор {self.generation} отключен")
        sleep(.3)
class Rom:
    def __init__(self, capasity, speed):
        self.capasity = capasity
        print(f"Диск {self.capasity}MB {speed}:", end = " ")
        sleep(.3)

        
        
class RomSsdM2(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"superfast")
        self.form = "m2"
        print("C:\> Рабочий диск подключен")
        sleep(.3)


    def load_sistem(self):
        print("C:\> загружается система")
        for i in range(20):
            print("*", end="")
            sleep(.5)
        print("*", end="\n")

    def turn_off(self):
        print("С:\> Системный диск выключен")
        sleep(.3)
        
class RomSsd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"fast")
        self.form = "2.5i"
        print("D:\> Рабочий диск подключен")
        sleep(.3)

    def turn_off(self):
        print("D:\> Рабочий диск выключен")
        sleep(.3)
        
class RomHdd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"middle")
        self.form = "3.5i"
        print("E:\> Архивный диск подключен")
        sleep(.3)

    def turn_off(self):
        print("E:\> Архивный диск выключен")
        sleep(.3)


class SystemBlock:
    def __init__(self):
        while True:
            if not (len(input("Включить компьютер?"))):
                break
            # else:
            #     print("Ну и не надо")
            #     exit(0)
        self.power = Power(220)
        self.power.turn_on()
        if self.power.power_on:
            self.motherboard = Motherboard("Asus")
            self.cpu = Cpu("Intel i7 6700")
            self.ram = Ram("32гб","DDR4")
            self.gpu = Gpu("Nvidia 960")
            self.sys_hdd = RomSsdM2(256)
            self.work_hdd = RomSsd(256)
            self.base_hdd = RomHdd(1024)
            self.sys_hdd.load_sistem()
            print("Hello Windows!")
        while True:
            if not (len(input("Выключите компьютер!"))):
                break
        self.base_hdd.turn_off()
        self.work_hdd.turn_off()
        self.sys_hdd.turn_off()
        self.ram.turn_off()
        self.gpu.turn_off()
        self.cpu.turn_off()
        self.motherboard.turn_off()

SystemBlock()
