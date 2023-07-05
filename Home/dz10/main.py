"""
Основная проблема - выбрать объект. Идеально была бы машина, но ее мы делали в
классе.
по этому объектом будет компьюер из следующего задания

    С помощью классов в python создать ПК порядок запуска
    1. Блок питания
    2. Мат плата
    3. Процессор
    4. Оперативная память
    5. Видеокарта
    6. Постоянная память (SSD HDD m2.ssd)
"""


def turn_on(name):
    print(f"{name} вкл.")


def turn_off(name):
    print(f"{name} выкл.")




Power = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "name": "Блок питания",
    "status":False,
}

Cpu = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "name": "Центральный процессор",
}

Ram = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "name": "Оперативная память",
}

Gpu = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "name": "Видеокарта",
}

Rom = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "name": "Винчестер",
}

Motherboard = {
    "turn_on": turn_on,
    "turn_off": turn_off,
    "cpu":Cpu,
    "ram":Ram,
    "gpu":Gpu,
    "rom":Rom,
    "name": "Материнская плата",
}


Atx = {
    "Power": Power,
    "Motherboard": Motherboard,
}


Atx["Power"]["turn_on"](Atx["Power"]["name"])
Atx["Motherboard"]["turn_on"](Atx["Motherboard"]["name"])
Atx["Motherboard"]["cpu"]["turn_on"](Atx["Motherboard"]["cpu"]["name"])
Atx["Motherboard"]["ram"]["turn_on"](Atx["Motherboard"]["ram"]["name"])
Atx["Motherboard"]["gpu"]["turn_on"](Atx["Motherboard"]["gpu"]["name"])
Atx["Motherboard"]["rom"]["turn_on"](Atx["Motherboard"]["rom"]["name"])
print()
Atx["Motherboard"]["rom"]["turn_off"](Atx["Motherboard"]["rom"]["name"])
Atx["Motherboard"]["gpu"]["turn_off"](Atx["Motherboard"]["gpu"]["name"])
Atx["Motherboard"]["ram"]["turn_off"](Atx["Motherboard"]["ram"]["name"])
Atx["Motherboard"]["cpu"]["turn_off"](Atx["Motherboard"]["cpu"]["name"])
Atx["Motherboard"]["turn_off"](Atx["Motherboard"]["name"])
Atx["Power"]["turn_off"](Atx["Power"]["name"])
