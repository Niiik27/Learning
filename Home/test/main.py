
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
# print(compare_with_ints())
# print("")


# a = (1,2,3)
# b = (1,2,3)
# print (a is b)