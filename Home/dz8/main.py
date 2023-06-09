guestList = []
max_limit = 100

while True:
    nameGuest = input("Введите имя гостя:> ")
    ageGuest = int(input("Введите возраст гостя:> "))
    infoGuest = {
        "nameGuest": nameGuest,
        "ageGuest": ageGuest,
    }
    guestList.append(infoGuest)
    if len(guestList)>3:break
for guest in guestList:
    print("--------------------------------------")
    print(f"Имя гостя - {guest['nameGuest']}")
    print(f"Возраст гостя - {guest['ageGuest']}")