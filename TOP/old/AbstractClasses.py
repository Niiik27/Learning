"""
Абстрактный класс
"""
from abc import ABC, abstractmethod, abstractproperty
# class Animal(ABC):
#     @abstractmethod
#     def __init__(self, name, sound) -> None:
#         self.name = name
#         self.sound = sound
    
#     def activeSound(self):
#         print(self.sound)
    
#     def showName(self):
#         print(self.name)

# class Cat(Animal):
#     def __init__(self, name) -> None:
#         super().__init__(name,"Мяу")

    
#     def purr(self):
#         print("Мурлыкает")

# class Dog(Animal):
#     def __init__(self, name) -> None:
#         super().__init__(name,"Ufd")

    
#     def dogHole(self):
#         print("Копает яму")


# class Donkey(Animal):
#     def __init__(self, name) -> None:
#         super().__init__(name, "Иа-иа")

# myCat = Cat("Вася")
# myCat.showName()
# myCat.purr()

# myDog = Dog("Рекс")
# myDog.showName()
# myDog.dogHole()

# # myDonkey = Animal("Осел","Иа-иа")#Класс Animal теперь абстрактный и нельязя создать напрямую экземпляр этого класса
# myDonkey = Donkey("Осел")
# myDonkey.activeSound()

# class Human(ABC):
#     @abstractmethod
#     def __init__(self, name, nationality) -> None:
#         self.name = name
#         self.nationality = nationality
#         print(self.name, self.nationality, self.gender)

# class Man(Human):
#     def __init__(self, name, nationality) -> None:
#         self.gender = "Мужской"
#         super().__init__(name, nationality)

# class Woman(Human):
#     def __init__(self, name, nationality) -> None:
#         self.gender = "Женский"
#         super().__init__(name, nationality)

# man = Man("Денис","Китаец")
# woman  = Woman("Оля","Немка")


class Grandfather(ABC):
    @abstractmethod
    def __init__(self, name, hairColor) -> None:
        self.name = name
        self.hairColor = hairColor
    @property
    # @abstractmethod
    def cookingBorsch(self):
        print("Готовил вкусный борщ")
    @abstractmethod

    def lezhalNaDivane(self):
        print("Этот метод обязаны определить в потомках")
# Ilya = Grandfather("Илья","Русый")
# Ilya.cookingBorsch()

class Father(Grandfather,ABC):
    def __init__(self, name, hairColor) -> None:
        self.name = name
        self.hairColor = hairColor

    def lezhalNaDivane(self):
        print("Лежал на диване")

    # def cookingBorsch(self):
    #     print("Готовил вкусный борщ!!!")


# class Baby(Father):
#     def __init__(self, name, hairColor) -> None:
#         self.name = name
#         self.hairColor = hairColor

Mixail = Father("Михаил","Рыжий")
Mixail.cookingBorsch
Mixail.lezhalNaDivane()

class Bird(ABC):
    @abstractmethod
    def __init__(self, name,sound) -> None:
        self.name = name
        self.sound = sound
    def eat():
        print("Кушает")
    def hunting(self):
        print("Охотятся")
    def activeSound(self):
        print(self.sound)


class NoFly(Bird,ABC):
    @abstractmethod
    def __init__(self, name,sound) -> None:
        super().__init__(name,sound)
    def walk(self):
        print("Ходит")

class Fly(NoFly,ABC):
    @abstractmethod
    def __init__(self, name,sound) -> None:
        super().__init__(name,sound)
    def fly(self):
        print("Летает")


class Crow(Fly):
    def __init__(self, name) -> None:
        super().__init__(name,"Кар-кар")

crow = Crow("Вася")
crow.fly()
crow.activeSound()


