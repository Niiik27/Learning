start_number = int(input("Введите двузначное число: "))


a=start_number//100
print(a)
b=start_number//10%10
print(b)
c=start_number%10%10%10
print(c)

print("Итого: "+str(a+b+c))








start_number = int(input("Введите двузначное число: "))
next_number=start_number
sum=0
k=100
x=next_number//k
next_number=start_number%k
sum=sum+x
print(x)

k=int(k/10)
x=next_number//k
next_number=start_number%k
sum=sum+x
print(x)

k=int(k/10)
x=next_number//k
next_number=start_number%k
sum=sum+x
print(x)
print("Итого: "+str(sum))



first_number = input("Введите первое число: ")
second_number = input("Введите второе число: ")
num=int(first_number+second_number)
print(num)



celsi = float(input("Введите температуру: "))
farengeit = celsi*9/5+32
print(farengeit)