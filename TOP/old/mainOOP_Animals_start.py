class Car:
    def __init__(self, color, mark, engine, transmission,wheel,light,audio, condey):
        self.color = color
        self.mark = mark
        self.engine = engine
        self.transmission = transmission
        self.wheel = wheel
        self.light = light
        self.audio = audio
        self.condey = condey
    
    def showColor(self):
        print(self.color)

    def showMark(self):
        print(self.mark)
    
    def showPow(self):
        print(self.engine.HP)

    def showVol(self):
        print(self.engine.capacity)


class SportCar(Car):
    def __init__(self, color, mark, engine, transmission,wheel,light,audio, condey, abs):
        super().__init__(color, mark, engine, transmission,wheel,light,audio, condey)
        self.abs = abs

    def showAbs(self):
        print(self.abs)
       






class Engine:
    def __init__(self, HP, capacity):
        self.HP = HP
        self.capacity = capacity

    def start(self):
        print("Запуск двигателя")

    def stop(self):
        print("Остановка двигателя")

    def showCapacity(self):
        print(self.capacity)
    def showPower(self):
        print(self.HP)



class SportEngine(Engine):
    def __init__(self, HP, capacity, turbo):
        super().__init__(HP, capacity)
        self.turbo = turbo

    def showTurbo(self):
        print(self.turbo)



class Transmission:
    def __init__(self, tr_type, num_step,) -> None:
        self.type = tr_type
        self.num_step = num_step
        self.speed = 0

    def showType(self):
        print(self.type)

    def showNumStep(self):
        print(self.num_step)

    def setSpeed(self,speed):
        self.speed = speed

    
class Wheel:
    def __init__(self,mark, diameter, pressure) -> None:
        self.mark = mark
        self.diameter = diameter
        self.pressure = pressure

    def move_right(self):
        print("Поворот на право")
    
    def move_left(self):
        print("Поворот на лево")

    def pump(self):
        self.pressure = 2.2
        print ("Колеса накачены")


class Light:
    def __init__(self,light_type) -> None:
        self.light_type = light_type

    def check_on(self):
        print("Включить фары")
    
    def check_of(self):
        print("Выключить фары")


class Audio:
    def __init__(self, pow,) -> None:
        self.pow = pow


    def showPower(self):
        print(self.pow)
        
    def playMusic(self):
        print("La-la-lala-laaaa!")


class Condey:
    def switch_on(self):
        print("Кондиционер включен")
        
    def switch_off(self):
        print("Кондиционер выключен")



myEngine = Engine(120,1.6)
sportEngine = SportEngine(280, 2.2, "Турбированный")

myTransmission = Transmission("Ручная", 5)
sportTransmission = Transmission("Автоматическая", 6)
myWheel = Wheel("Бриджстоут", 15,1)

myLight = Light("LED")
myAudio = Audio("50W")
myCondey = Condey()
myAuto = Car("green","audi",myEngine,myTransmission,myWheel,myLight,myAudio, myCondey)
myAuto.engine.showCapacity()
myAuto.engine.showPower()
myAuto.engine.start()
myAuto.transmission.showType()
myAuto.wheel.move_left()
myAuto.wheel.pump()
myAuto.light.check_on()
myAuto.audio.playMusic()
myAuto.condey.switch_on()


sportCar = SportCar("Blue","Ferrary",sportEngine,sportTransmission,myWheel,myLight,myAudio, myCondey, "Есть АБС")
print(sportCar.color)
sportCar.showMark()
sportCar.showAbs()
sportCar.engine.showTurbo()
sportCar.engine.showPower()



class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound
    
    def activeSound(self):
        print(self.sound)
    
    def showName(self):
        print(self.name)

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name,"Мяу")

    
    def purr(self):
        print("Мурлыкает")

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name,"Ufd")

    
    def dogHole(self):
        print("Копает яму")

myCat = Cat("Вася")
myCat.showName()
myCat.purr()

myDog = Dog("Рекс")
myDog.showName()
myDog.dogHole()