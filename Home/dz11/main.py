"""
    С помощью классов в python создать ПК порядок запуска
    1. Блок питания
    2. Мат плата
    3. Процессор
    4. Оперативная память
    5. Видеокарта
    6. Постоянная память (SSD HDD m2.ssd)
"""
class Power:
    def __init__(self, power):
        self.power = power
        print(f"Питание {self.power} вольт включено")
        
class Motherboard:
    def __init__(self, name):
        self.name = name
        print(f"Материнская {self.name} плата запитана")
    
class Cpu:
    def __init__(self, name):
        self.name = name
        print(f"Центральный процессор {self.name} активирован")
        
        
class Ram:
    def __init__(self, capasity, speed):
        self.capasity = capasity
        print(f"ОЗУ {self.capasity} {speed} активирована")
        
        
class Gpu:
    def __init__(self, generation):
        self.generation = generation
        print(f"Графический процессор {self.generation} активирован")

class Rom:
    def __init__(self, capasity, speed):
        self.capasity = capasity
        print(f"ПЗУ {self.capasity} {speed}:")
        
        
class RomSsdM2(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"superfast")
        self.form = "m2"
        print("C:\> загружается система")
        
class RomSsd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"fast")
        self.form = "2.5i"
        print("D:\> Рабочий диск подключен")
        
class RomHdd(Rom):
    def __init__(self, capasity):
        super().__init__(capasity,"middle")
        self.form = "3.5i"
        print("E:\> Архивный диск подключен")

class SystemBlock:
    def __init__(self):
        self.power = Power(220)
        if self.power.power == 220:
            self.motherboard = Motherboard("Asus")
            self.cpu = Cpu("Intel i7 6700")
            self.ram = Ram("32гб","DDR4")
            self.gpu = Gpu("Nvidia 960")
            self.sys_hdd = RomSsdM2(256)
            self.work_hdd = RomSsd(256)
            self.base_hdd = RomHdd(1024)
            print("Hello Windows!")
        else:
            print("Проблемы с электричеством")
SystemBlock()