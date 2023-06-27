# infoProduct = {
#     "nameProduct":"Каша",
#     "price":120,
#     "sale":0.2
# }
# print(infoProduct["nameProduct"],infoProduct["price"],infoProduct["sale"],sep="\n")

# print(f"{infoProduct['nameProduct']}\n{infoProduct['price']}\n{infoProduct['sale']}")

# myName = input("Введите свое имя ")
# myAge = int(input("Сколько вам лет "))
# infoPerson = {
#     "namePerson":myName,
#     "agePerson": myAge,
#     "hobbyPerson":["Sport", "Programming"]
# }

# print(infoPerson["hobbyPerson"][0])

# for key in infoPerson:
#     print(key)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# productList = [
#     {
#         "nameProduct": "Хлеб",
#         "price": 55,
#         "count": 37,
#         "category":"Выпечка",
#     },

#     {
#         "nameProduct":"Молоко",
#         "price": 101,
#         "count": 3,
#         "category":"Молочная",
#     },
#     {
#         "nameProduct":"Кефир",
#         "price": 99,
#         "count": 20,
#         "category":"Молочная",
#     },
#     {
#         "nameProduct":"Ряженка",
#         "price": 60,
#         "count": 10,
#         "category":"Молочная",
#     },
# ]

# for i in range(0,len(productList)):
#     print ("Инфо о товаре:")
#     # if productList[i]["price"]<80:
#     if productList[i]["category"]=="Молочная":
#         productList[i]['price'] *= 2
#         print(f"Категория - {productList[i]['category']}")
#         print(f"Название товара - {productList[i]['nameProduct']}")
#         print(f"Цена - {productList[i]['price']}")
#         print(f"Кол-во - {productList[i]['count']}")
#         print("--------------------------------------")
guestList = []

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

