


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