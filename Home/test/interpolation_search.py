from random import randint
arr = [randint(50, 8000) for i in range(1000000)]
arr = sorted(arr)
# arr = [1, 1, 4, 4, 4, 4, 6, 8, 9, 12, 15, 15, 18, 18, 19, 19, 19, 20, 21, 22, 23, 24, 24, 26, 27, 28, 29, 29, 29, 30, 31, 32, 34, 34, 34, 35, 35, 36, 36, 38, 39, 40, 41, 41, 41, 42, 43, 43, 43, 43, 44, 44, 45, 45, 46, 47, 48, 48, 48, 49, 50, 51, 51, 52, 52, 53, 53, 53, 53, 54, 58, 58, 60, 60, 62, 62, 63, 63, 63, 63, 63, 63, 64, 65, 65, 66, 67, 68, 68, 69, 70, 71, 73, 74, 74, 75, 78, 78, 79, 80]
# arr = [0, 0, 1, 3, 4, 6, 7, 11, 12, 14, 15, 15, 16, 19, 19, 20, 24, 24, 24, 25, 25, 25, 28, 28, 29, 29, 30, 31, 31,
#        31, 32, 35, 35, 36, 36, 36, 37, 39, 43, 43, 44, 44, 44, 45, 46, 47, 48, 50, 50, 50, 52, 52, 52, 53, 54, 55,
#        56, 57, 58, 58, 59, 60, 60, 60, 61, 61, 61, 62, 62, 63, 63, 65, 66, 68, 69, 70, 70, 71, 71, 71, 72, 72, 73, 73,
#        73, 74, 75, 75, 75, 75, 75, 75, 76, 76, 76, 77, 78, 79, 80, 80]
# arr = [1, 2, 2, 3, 5, 6, 6, 6, 7, 7, 9, 10, 11, 11, 12, 13, 13, 15, 15, 15, 16, 16, 18, 18, 19, 19, 20, 20, 20, 22,
#        24, 25, 25, 27, 27, 27, 28, 29, 31, 32, 34, 35, 35, 36, 36, 36, 36, 37, 41, 41, 43, 43, 43, 44, 44, 45, 46,
#        48, 48, 51, 51, 52, 53, 53, 53, 55, 57, 57, 59, 60, 60, 61, 61, 62, 63, 63, 63, 64, 64, 64, 64, 64, 64, 65,
#        65, 67, 70, 72, 74, 75, 77, 77, 77, 78, 78, 78, 78, 79, 79, 79]
x = arr[10000]
print(x)
# arr = [2, 3, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 20, 21, 21, 25, 25, 26,
#        27, 29, 30, 34, 34, 34, 35, 38, 38, 41, 42, 43, 46, 47, 49, 49, 50, 51, 51, 51, 51, 52, 53, 54, 55, 55, 55,
#        56, 57, 57, 59, 65, 67, 70, 71, 72, 73, 74, 75, 75, 76, 76, 76, 76, 78, 79, 81, 85, 86, 86, 87, 87, 88, 88,
#        88, 90, 91, 92, 92, 93, 95, 96, 96, 96, 96, 98, 98, 98, 99, 99]
# print("index of X",arr.index(x))
# first_arr = [i for i in range(15,100)]
# second_arr = [i for i in range(len(first_arr)+1,len(first_arr)+100)]
# third_arr = [i for i in range(len(first_arr)+len(second_arr)+2,len(first_arr)+len(second_arr)+100)]
# arr=[*first_arr,*[99,99,99],*second_arr,*third_arr]
# arr = first_arr
# print(arr)


max_iteration = 10
iteration = max_iteration
# guess_index = int((end_val - start_val) / len(arr) * x + start_val) + 1
# guess_start_index = int((end_val - start_val) / len(arr) * (x - start_val))

start_index = 0
old_start_index = start_index
end_index = len(arr) - 1
old_end_index = end_index
supposed_pos = 0
old_supposed_pos = supposed_pos



while True:
    iteration -= 1
    start_val = arr[start_index]
    end_val = arr[end_index]
    # supposed_start_index += int((end_val - start_val) / len(arr) * (x - start_val))
    # Нужно прикинуть где в массиве может находится искомое число, исходя из его значения и диапазона массива
    supposed_step_of_list = (end_val - start_val) / (end_index - start_index + 1)
    # Массив может начинаться не с 0, а значит нужно искать позицию относительно началат
    # Это приблизительная позиция, а значит она может быть +-1
    # Но при вычислении позици можно впасть в рекурсию, если не будет изменения индекса
    # По этому принудительно сдвигаю позицию на -1
    # supposed_pos = int(round((x - start_val) / supposed_step_of_list)) + start_index + int(old_supposed_pos == supposed_pos)*(1-int(x<arr[supposed_pos])*2)
                                                                            # + x>supposed_pos;  - x<supposed_pos
    supposed_pos = int((x - start_val) / supposed_step_of_list) + start_index
    if old_supposed_pos == supposed_pos:
        supposed_pos += (1 - int(x < arr[supposed_pos]) * 2)
    # supposed_pos += int((end_val - start_val) / len(arr) * (x - start_val))
    old_supposed_pos = supposed_pos
    # if supposed_pos == old_supposed_pos:
    #     supposed_pos=supposed_pos-1
    #     old_supposed_pos = supposed_pos
    # Если искомое число поделиь на шаг, то получим индекс
    # print("start_val", start_val)
    # print("end_val", end_val)
    # print("supposed_step_of_list", supposed_step_of_list)
    print("start_index", start_index)
    print("end_index", end_index)
    print("supposed_pos", supposed_pos)
    # print("arr[supposed_pos]", arr[supposed_pos])
    print("--------------------------------------------------")

    if x == arr[supposed_pos]:
        # Этот вайл нужен на тот случай, если в массиве есть повторяющиеся значения, а мы его нашли справа,
        # или с середины. Тогда если нас интересует первое вхождение, то нам нужно отмотать влево, пока не упремся в
        # другое значение, а затем вернемся на один шаг вправо
        # решение плохо тем что прибегает к простой итерации, а должен быть бинарный, интерполяционный, или еще какой-
        # нибудь быстрый поиск. При нобольшом количестве одинаковых значений - проще итерироваться данным вайлом. А при
        # большом нужен поиск получается мы должны либо заранее знать, что элементов будет много и нужно устраивать,
        # хитрый поиск, либо придумать метод определяющий предпочтительный способ. Например все что в пределах
        # 10 итераций - решать перебором, все что больше - решать поиском
        # Тогда сначала определяем - нашли ли мы элемент двигаясь справа или угадали спервого раза. Если так, то нужно
        # взять элемент на 10 позиций левее. Если он равен найденому, значит все плохо и нужен бинарный поиск, если нет,
        # то проверяем элемент слева от найденного - данным вайлом.
        # для плохого варианта подойдет только бинарный поиск так как интерполяция будет вырожденной, и спровоцирует
        # тупой перебор
        # нехватает выхода без результата
        while x == arr[supposed_pos]:
            supposed_pos -= 1
        supposed_pos += 1
        print("supposed_pos FINDED", supposed_pos)
        print([arr[supposed_pos]])
        break

    # На предполагаемой позиции может оказаться число либо больше искомого, либо меньше и тогда нужно продолжить поиск
    # Если число больше то это значит что не нужно искать за пределами этого числа, и поиск нужно повторить в диапазоне
    # до этого числа
    # А если число меньше искомого, то нужно повторить поиск от этого числа
    elif x > arr[supposed_pos]:
        start_index = supposed_pos# - int(start_index == old_start_index)
        # old_start_index = start_index
    elif x < arr[supposed_pos]:
        end_index = supposed_pos #+ int(end_index == old_end_index)
        # old_end_index = end_index

    if not iteration: break
print("iteration", max_iteration - iteration)

