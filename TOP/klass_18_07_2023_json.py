import json
base_list = [
    {
        "id":1,
        "firstname": "Николай",
        "lastname": "Меньшиков",
        "birthday": "27.10.1980",
        "gender": "Мужской",
        "login": "Niiik27",
        "password": "12345",
    },
    {
        "id":2,
        "firstname": "Денис",
        "lastname": "Кириллов",
        "birthday": "01.06.2001",
        "gender": "Мужской",
        "login": "Denis161",
        "password": "54321",
    },
    {
        "id":3,
        "firstname": "Екатерина",
        "lastname": "Исаева",
        "birthday": "25.10.2000",
        "gender": "Женский",
        "login": "Ekaterina25",
        "password": "11111",
    },
    {
        "id":4,
        "firstname": "Ольга",
        "lastname": "Владимирова",
        "birthday": "22.11.1999",
        "gender": "Женский",
        "login": "Olya22",
        "password": "22222",
    },
    {
    "id":5,
        "firstname": "Кирилл",
        "lastname": "Кириллов",
        "birthday": "17.11.2006",
        "gender": "Мужской",
        "login": "Kirillooo",
        "password": "55555",
    },
]

registered_users = []

# fileW = open('base.json', "w", encoding="utf-8")
# fileW.write(json.dumps(base_list))
# fileW.close()

fileR = open('base.json', "r", encoding="utf-8")

# primer = '[{"first_name":"Denis","age":22},{"first_name":"Masha","age":18}]'

base_list_read = fileR.read()
print(base_list_read)
new_base = json.loads(base_list_read)
new_base_json = json.dumps(new_base,ensure_ascii=False)
print(new_base_json)



