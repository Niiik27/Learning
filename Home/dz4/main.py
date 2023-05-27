
print("Домашнее задание №4 - Циклы")
print("")
print("Упражнение №1 - определить кратность 7 в указанном диапазоне")
inputString = input("Укажите диапазон в формате ОТ-ДО ")
division = 7
custom_division = input("Укажите требуемую кратность или пропустите этот шаг ")
if len(custom_division) !=0:
    division = int(custom_division)
start_str = ""
end_str = ""
start_geted = False
for symbol in inputString:
    if start_geted == False:
       if symbol != "-":
            start_str+=symbol
       else:
           start_geted = True
    elif start_geted:
        end_str+=symbol
# print(start_str,end_str)
start = int(start_str)
end = int(end_str)+1
res=""
for i in range(start,end):
    if i % division == 0:
            res+=(str(i)+", ")
trim_res=""
for i in res:
     if len(trim_res)+2==len(res): break
     trim_res+=i
     
print(f"Числа кратные {division} в диапазоне от {start} до {end_str}: {trim_res}")


print("")

print("Упражнение №2 - определить все числа диапазона, в обратном порядке, кратные 7, количество кратных 5")
inputString = input("Укажите диапазон в формате ОТ-ДО ")
division = 7
five_division = 5
custom_division = input("Укажите требуемую кратность или пропустите этот шаг ")
if len(custom_division) !=0:
    division = int(custom_division)
start_str = ""
end_str = ""
start_geted = False
for symbol in inputString:
    if start_geted == False:
       if symbol != "-":
            start_str+=symbol
       else:
           start_geted = True
    elif start_geted:
        end_str+=symbol
# print(start_str,end_str)
start = int(start_str)
end = int(end_str)+1
res=""
range_str = ""
last_num=0
for i in range(start,end):
    last_num+=1
    range_str+= str(i)

    if last_num<end-start:
        range_str+=", "

print(f"Все числа диапазона: {range_str}")
range_str=""
last_num=0
for i in range(end-1,start-1,-1):
    last_num+=1
    range_str+= str(i)

    if last_num<end-start:
        range_str+=", "

print(f"Все числа диапазона в обратном порядке: {range_str}")

for i in range(start,end):
    if i % division == 0:
            res+=(str(i)+", ")
trim_res=""
for i in res:
     if len(trim_res)+2==len(res): break
     trim_res+=i
     
print(f"Числа кратные {division} в диапазоне от {start} до {end_str}: {trim_res}")

five_num=0
five_str=""
for i in range(start,end):
    if i % five_division == 0:
            five_num+=1
            five_str+=(str(i)+", ")
trim_res=""
for i in five_str:
     if len(trim_res)+2==len(five_str): break
     trim_res+=i

print(f"Количество чисел кратных {five_division} в диапазоне от {start} до {end_str}: {five_num}")
print(f"Кратные {five_division}: {trim_res}")

print("")
print("Упражнение №3 - Fizz Buzz")
inputString = input("Укажите диапазон в формате ОТ-ДО ")
three_division = 3
five_division = 5

start_str = ""
end_str = ""
start_geted = False
for symbol in inputString:
    if start_geted == False:
       if symbol != "-":
            start_str+=symbol
       else:
           start_geted = True
    elif start_geted:
        end_str+=symbol
# print(start_str,end_str)
start = int(start_str)
end = int(end_str)+1
res=""
for i in range(start,end):
    if i % three_division == 0:
            res+="Fizz "
    if i % five_division == 0:
            res+="Buzz "
    if len(res) == 0:
         res = str(i)
    print(res)
    res=""
print("")
print("Фибоначи")
input_num = int(input("Введите предел для поиска чисел Фибоначи "))+1
num_before=1
next_num=2
print("Для числа 0 пропорция золотого сечения: 0")
print("Для числа 1 пропорция золотого сечения: 1")

while next_num<input_num:
     print(f"Для числа {next_num} пропорция золотого сечения: {next_num/num_before}")
     old_next_num = next_num
     next_num+=num_before
     num_before=old_next_num
  
# for i in range(3,input_num):
#      old_next_num = next_num
#      next_num=num_before+next_num
#      if next_num>input_num: break
#      num_before=old_next_num
#      print(f"Для числа {next_num} пропорция золотого сечения: {next_num/num_before}")


print("В указанном пределе больше нет чисел Фибоначи")    

