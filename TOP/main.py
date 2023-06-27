"""
Дилегирование и мышление ООП
"""
#Создание персонажа
def attack(act):
    print(act)

Person = {
    "name": "Варвар",
    "gender":"Мужской",
    "actions":{
        "attack":attack,
    }
}

# Создание объекта на основе персонажа
Human = Person.copy()
Human["race"] = "Человек"
Human["skills"] = ["Быстрый бег","Красноречие"]



Archer = Human.copy()
Archer ["role"] = "Воин"
Archer ["desc"] = "Лучники способны избегать все эффекты контроляи(кроме Эриолы) и получать меньше входящего урона, что позволяет\
им дольше житть и беспрепятственно вносить ДПС."
Archer ["actions"]["attack"] = attack
Archer ["actions"]["attack"]("Стрельба из лука")

Ork = Person.copy()
Ork["race"] = "Орк"
Ork["skills"] = ["Сила","Груборечие"]
Ork ["actions"]["attack"]("Удар")

Warrior = Ork.copy() or Human.copy()
Warrior ["role"] = "Воин"
Warrior ["desc"] = "Воин отличается своим сочетанием мобильности, живучести, способности наносить урон и прерывать противника."
Warrior ["actions"]["attack"]("Удар")

Shaman = Ork.copy()
Shaman ["role"] = "Шаман"
Shaman ["desc"] = "Шаманы - наставники в духовных практиках, идущих не от Бога, а от самих природных стихий"
Shaman ["actions"]["attack"]("Закленание")
print("---------------------------")
print("Персонаж",Person,"\n","---------------------------")
print("Человек",Human,"\n","---------------------------")
print("Воин",Warrior,"\n","---------------------------")
print("Лучник",Archer,"\n","---------------------------")
print("Шаман",Shaman,"\n","---------------------------")
print("Персонаж",Ork,"\n","---------------------------")



exit(0)
def start():
    print("Запуск")
def stop():
    print("Стоп")

Engine = {
    "start":start,
    "stop":stop,
}
# Engine["start"]()
# Engine["stop"]()

def open():
    print("Капот открыт")
def close():
    print("Капот закрыт")
Bonnet = {
    "open":open,
    "close":close,
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
