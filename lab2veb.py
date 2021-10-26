import time
t=2
def decorator(count):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}::{args}::{kwargs}"
            cached_value = cache.get(key)
            if cached_value is None:
                res = func(*args, **kwargs)
                cache[key] = {"count": count, "value": res}
                return res
            else:
                counter = cached_value["count"]
                value = cached_value["value"]
                counter -= 1
                cache[key] = {"count": counter, "value": value}
                if counter <=0:
                    cache.pop(key)
                return value
        return wrapper
    return outer_wrapper

def Pal(x):
    temp_x = x
    rev = 0
    while(x > 0):
        dig = x % 10
        rev = rev * 10 + dig
        x = x // 10
    if (temp_x == rev):
        return True
    else:
        return False

def Del(l):
    a = []
    b = []
    c = []
    for i in l:
        if i % 2 == 0:
            a.append(i)
        if i % 3 == 0:
            b.append(i)
        if i % 5 == 0:
            c.append(i)
    return a, b, c
def Rev(x):
    rev_x = 0
    if(x > 0):
        while(x > 0):
            dig = x % 10
            rev_x = rev_x * 10 + dig
            x = x // 10
    elif(x < 0):
        x = x - 2*x
        while(x > 0):
            dig = x % 10
            rev_x = rev_x * 10 + dig
            x = x // 10
        rev_x = rev_x - 2 * rev_x
    return rev_x

@decorator(count=t)
def Newt(a,n):
    pog = 0.001
    root = a / n
    rn = a
    while abs(root-rn) >= pog:
        rn = a
        for i in range(1,n):
            rn = rn / root
        root = 0.5 * (rn + root)
    return root
def Simp(a):
    while a<0 or a>100000:
        print('wrong num, enter again')
        a=int(input())
    x = 2
    while a % x != 0:
        x+=1
    return x == a





while 1:
    cache = {}
    print('choose func ')
    x=input()
    if x == '0':
        print('enter number')
        print(Pal(int(input())))
    elif x == '1':
        l=[]
        print('enter 10 numbers')
        for i in range(10):
            l.append(int(input()))
        print(Del(l))
    elif x == '2':
        print(Rev(int(input())))
    elif x == '3':
        print('enter num of iterations')
        o=int(input())
        print('enter number to root(more is longer)')
        a=int(input())
        print('enter power of root(more is much longer)')
        n=int(input())
        for i in range(o):
            start_time = time.time()
            print(Newt(a,n))
            end_time = time.time()
            time_elapsed = (end_time - start_time)
            print('time elapsed:',time_elapsed)
    elif x == '4':
        print('enter number')
        print(Simp(int(input())))
    else:
        break
