# from random import randint

# arr = [randint(0, 100) for i in range(100)]
# arr = sorted(arr)

# Для работы кода требуется упорядоченный массив, не обязателен одинаковый шаг между элементами, и возможны повторения


arr = list(range(100))
x = 23
start_point = len(arr) - 1
end_point = int(start_point // 2)
iteration = 0
while arr[start_point] > x:
    while arr[end_point] > x:
        iteration += 1
        start_point = end_point
        end_point = int(end_point // 2)
    else:
        iteration += 1
        if arr[end_point] == x:
            break
        elif start_point - end_point == 1:
            break
        elif iteration > 100:# Защита от зависания, если что то пошло не так
            break
        end_point += (start_point - end_point) // 2

if arr[end_point] == x:
    print("index", end_point)
else:
    print("has not in list", -1)
print('iteration', iteration)