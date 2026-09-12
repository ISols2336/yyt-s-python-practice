def add(*args):                     #求数字和函数
    total = 0
    for i in args:
        if type(i) in(int,float):
            total += i

    return total


def dict(**arg):                    #字典生成函数
    di = arg
    return di

def dice(n = 5):                    #投骰子函数
    import random
    total = 0
    for _ in range(n):
        total += random.randrange(1,7)

    return total

def factorial_1(y):               #计算阶乘函数
    res = 1
    for x in range(1,y+1):
        res *= x
    return res

def f_1():                      #计算组合数函数
    m = int(input('请输入m'))
    n = int(input('请输入n'))

    num = factorial_1(m)//(factorial_1(n)*factorial_1(m-n))
    print(num)
