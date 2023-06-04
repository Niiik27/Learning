print("Домашняя работа №6 часть 2 - строки, списки")
list_1 = [3,3,1,3,7,9,5,4,2,8,6]
list_2 = [12,3,4,7,13,6,2,1,0,4]
print(f"Массив №1: {list_1}")
print(f"Массив №2: {list_2}")

print("Объединение массивов:")
#Можно былобы использовать связку for list_2 + append, но тут напрашивается конкатенация.
# а для подобной связки есть последующие задания
list_sum = list_1+list_2
print(f"Элементы обоих списков в одном массиве: {list_sum}")

print("Объединение массивов без повторений:")
list_collect = []
for i in list_1:
    added = False
    for n in list_collect:
        if n == i:
            added = True
            break
    if added == False:
        list_collect.append(i)
for i in list_2:
    added = False
    for n in list_collect:
        if n == i:
            added = True
            break
    if added == False:
        list_collect.append(i)
print(f"Элементы обоих списков в одном массиве без повторений: {list_collect}")


#Здесь по сложнее так как в обоих массивах могут оказаться дублирующиеся элементы, а значит они могут
#добавиться более одного раза
print("Выборка общих элементов:")
cross_list_collect = []
for i in list_1:
    for n in list_2:
        if n == i:
            added = False
            for m in cross_list_collect:
                if n == m:
                    added = True
                    break

            if added == False:
                cross_list_collect.append(n)
                break

print(f"Общие элементы в обоих списках: {cross_list_collect}")




print("Выборка уникальных элементов:")
unique_list_collect = []
for i in list_1:
    duble = False
    for n in list_2:
        if n == i:
            duble = True
            break
            
    if duble == False:
        added = False
        for m in unique_list_collect:
            if i == m:
                added = True
                break

        if added == False:
            unique_list_collect.append(i)
#Добавили уникальные элементы только из первого массива
#Теперь придется добавлять уникальные элементы из второго массива

for i in list_2:
    duble = False
    for n in list_1:
        if n == i:
            duble = True
            break
            
    if duble == False:
        added = False
        for m in unique_list_collect:
            if i == m:
                added = True
                break

        if added == False:
            unique_list_collect.append(i)

print(f"Уникальные элементы в обоих списках: {unique_list_collect}")



print("Оставить только min max:")
#Возможно не правильный подход на данном этапе, ноо метод sort уже доступен
list_1.sort()
list_2.sort()
min_max = [list_1[0],list_1[len(list_1)-1],list_2[0],list_2[len(list_2)-1]]
print(f"min max: {min_max}")

#Теперь попробую решить задачу циклом
min_1=list_1[0]
max_1=list_1[0]
for n in list_1:
    min_1 = min_1 if min_1<n else n
    max_1 = max_1 if max_1>n else n
min_2=list_2[0]
max_2=list_2[0]
for n in list_2:
    min_2 = min_2 if min_2<n else n
    max_2 = max_2 if max_2>n else n
min_max = [min_1,max_1,min_2,max_2]
print(f"min max: {min_max}")

#Наверное можно прибегнуть к функциям min max так как они показываются в подсказках при объявлении переменных
print(f"min max: {[min(list_1),max(list_1),min(list_2),max(list_2)]}")
