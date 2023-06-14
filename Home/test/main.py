checked_users = {}
next_user = 0

lessonDays = ["Четверг","Пятница"]
users = [
    "Денис Игоревич",
    "Меньшиков",
    "Выборнов",
    "Курочкин",
    "Мухитов",
    "Попов",
    "Чепаксин",
    "Карпов",
    "Соколов",
    "Захаров",
    "Казаков",
    "Хисамов",
]

if len(checked_users) <= len(users):

    userSurname = ""
    while userSurname not in users:
        userSurname = input("Если вы студент, то введите свою фамилию, если преподаватель, то имя отчество> ")
        if userSurname in users:
            break
        print ("Нет такого пользователя! ")
    if users.index(userSurname)>next_user:
        print("Ждите своей очереди. Вам должны прислать две строки, которыми вы замените первые две строчки кода.")
        exit(0)

    days_str = ""
    for i in range(len(lessonDays)):
        days_str+=f"{i+1} - {lessonDays[i]}\n"

    choice = int(input(f"{users[next_user]} выберите день недели:\n{days_str}>"))-1
    checked_users[users[next_user]] = choice
    if next_user + 1 < len(users):
        print(f"{users[next_user]} отправте эти строчки {users[next_user+1]}у для замены первых двух строчек кода:")
        next_user += 1
        print(f"checked_users = {checked_users}")
        print(f"next_user = {next_user}")
    else:
        forthday_num = 0
        frighday_num = 0
        next_lesson = ""
        for key in checked_users:
            if checked_users[key] == 0:
                forthday_num += 1
            else:
                frighday_num += 1
        next_lesson = "Четверг" if forthday_num > frighday_num else "Пятница"
        print("Опубликуйте результат: ")
        print(f"Следующее занятие будет в {next_lesson}")
exit(0)





list_1 = [3,3,1,3,7,9,5,4,2,8,6]
list_2 = [12,3,4,7,13,6,2,1,0,4]

collection =set(list_1)
collection.update(list_2)
print(f"Элементы обоих списков в одном массиве без повторений: {list(collection)}")

collection =set(list_1)
collection.intersection_update(list_2)
print(f"Общие элементы в обоих списках: {list(collection)}")

collection = set(list_1)
collection.symmetric_difference_update(list_2)
print(f"Уникальные элементы в обоих списках: {list(collection)}")







numberList = [2,3,1,3,6,7,9,5,4,2,8,6]
print(numberList)

while True:
    del_odd = False
    start = 0
    for i in range(start,len(numberList)):
        # numberList[i]=numberList[i]**2
        # print(numberList[i])
        if numberList[i]==2:
            numberList.pop(i)
            del_odd = True
            start=i
            break
    if del_odd == False: break

    
print(numberList)
numberList.sort()

exit(0)
import time
# print(time.time())
# print(time.perf_counter_ns())

def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f"{function.__name__}{args}:", time.time() - start_time)
        return res
    return wrapped


# def func(first, second):
#     return bin(int(first, 2) + int(second, 2))


@time_of_function
def compare_with_strings(x,y):
    c=0
    a = "sdfjhgslkdjfg sldfjghlsdfhgkljsd sdljfghsdlfjghsdfl sdlfjghdfjslhglsdjf"
    b = "lkjdsfhgdsfjl lsdfjkghsdfjklghsd lsdfkjhgsdfljhgjlksdf sldffkfhgdflkghf"
    for i in range(1000000):
        if a!=b:
            c*=c
    return "qwerty"
@time_of_function
def compare_with_ints():
    c=0
    a = 1
    b = 2
    for i in range(1000000):
        if a!=b:
            c*=c

print(compare_with_strings(1,2))
a="hellow word"
b="hellow"+" word"
print(a is b)
# print(compare_with_ints())
# print("")


# a = (1,2,3)
# b = (1,2,3)
# print (a is b)