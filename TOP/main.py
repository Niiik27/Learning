"""
Дилегирование и мышление ООП
"""
def Car(marka, color, engine):
    thisMarka = marka
    thisColor = color
    thisEngine = engine


def Engine():
    def start():
        print("Запуск")
    def stop():
        print("Стоп")

auto = Car("audi","green", Engine)
print(auto)