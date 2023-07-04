def start():
    print("Запуск")


def stop():
    print("Стоп")


Engine = {
    "start": start,
    "stop": stop,
}


# Engine["start"]()
# Engine["stop"]()

def open():
    print("Капот открыт")


def close():
    print("Капот закрыт")


Bonnet = {
    "open": open,
    "close": close,
}
Car = {
    "color": "",
    "mark": "",
    # "Engine":"",
    # "Bonnet":"",
}

auto = Car.copy()
print(auto)
# exit(0)
auto["color"] = "green"
auto["mark"] = "Audi"
auto["Engine"] = Engine
auto["Bonnet"] = Bonnet
auto["doors"] = 4

auto["Engine"]["start"]()
auto["Engine"]["stop"]()
auto["Bonnet"]["open"]()
auto["Bonnet"]["close"]()
print("Мое авто", auto)
print("Какое то авто", Car)
