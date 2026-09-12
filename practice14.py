#知识点：def 定义函数、参数（位置/关键字/默认值/*args/**kwargs）、import
#输入m和n，计算组合数C(m,n)的值
#C(m,n) = m! / (n! * (m-n)!)，即从 m 个里选 n 个有多少种选法

def function ():
    m = int(input('请输入m'))
    n = int(input('请输入n'))

    res_1 = 1              #m 的阶乘
    for x in range(1,m+1) :
        res_1 = res_1 * x

    res_2 = 1              #n 的阶乘
    for y in range(1,n+1) :
        res_2 = res_2 * y

    res_3 = 1              #(m-n) 的阶乘；n 比 m 大时 range 为空，结果会算错
    for z in range(1,m-n+1) :
        res_3 = res_3 * z

    res_end = res_2*res_3   #分母：n! * (m-n)!

    print(res_1//res_end)   #// 整除，商正好是组合数

function()   #真正执行的地方：调用函数


#重构代码使其更加简洁：把三段阶乘抽成一个函数

def factorial_1(y):               #计算阶乘
    res = 1
    for x in range(1,y+1):        #已修好：循环变量 x、参数 y 不同名，参数不会再被覆盖
        res *= x
    return res

def f_1():                      #计算组合数C(m,n)的值
    m = int(input('请输入m'))
    n = int(input('请输入n'))

    num = factorial_1(m)//(factorial_1(n)*factorial_1(m-n))
    print(num)

f_1()


#导入：直接用标准库的 factorial，比自己写还快
from math import factorial as fac   #也可用 import math，as 给函数起别名 fac

m = int(input('请输入m'))
n = int(input('请输入n'))

print(fac(m)//(fac(n)*fac(m-n)))


#位置参数：按从左到右的顺序依次对应
def make_triangle(a,b,c) :
    print(a + b > c and a + c > b and b + c > a )  #判断三边是否组成三角形

make_triangle(1,2,3)      #False

#关键字参数：参数名=值，顺序可以打乱
make_triangle(c = 1,a = 5,b = 5)    #True
#make_triangle(x = 1,y = 2,z = 3)   #报错：参数名不匹配（没有 x/y/z 这些参数）

#限定传参方式：/ 左边只能位置传参；* 右边只能关键字传参
def make_triangle_1(a,b,c,/) :
    print(a + b > c and a + c > b and b + c > a )

def make_triangle_2(*,a,b,c,) :
    print(a + b > c and a + c > b and b + c > a )

make_triangle_1(3,4,5)    #True
#make_triangle_1(a = 3,b = 4,c = 5)    #TypeError：/ 前的参数不能用关键字传

make_triangle_2(a = 3,b = 4,c = 5)     #True
#make_triangle_2(3,4,5)                #TypeError：* 后的参数必须用关键字传


#参数的默认值：调用时可省略，省略就用默认值
from random import randrange as ra

def dice(n = 5):
    total = 0
    for _ in range(n):
        total += ra(1,7)       #randrange(1,7) 是 1 到 6

    return total

print(dice())     #不传参，n 默认 5
print(dice(3))    #传 3，用 3

def make_triangle_3(a = 3,b = 4,c = 5) :
    bools = a + b > c and a + c > b and b + c > a
    return bools


print(make_triangle_3(1,1,2))    #位置传参，前两个覆盖默认值
print(make_triangle_3(a = 1, b = 1, c = 2))   #关键字传参

#默认值规则：
#① 无默认值的参数必须写在带默认值参数前面：def func(a, c, b=10)
#② 位置传参按顺序对应：func(1,2) → a=1, c=2, b 用默认 10
#③ 关键字传参可打乱顺序：func(a=1, c=2, b=20)


#可变参数
def add(*args):           #*args：接收任意个位置参数，打包成元组
    total = 0
    for i in args:
        if type(i) in(int,float):   #只累加数字，跳过其他类型
            total += i

    return total          #已修好：原来是 return all（内置函数），应返回 total

print(add(12,34,53))   #99
#print(add(a = 1,b = 1))   #TypeError：*args 不接收关键字参数

def dict(**arg):        #**arg：接收任意个关键字参数，打包成字典；函数名 dict 覆盖了内置 dict，建议改名
    di = arg
    return di

print(dict(device = "RaspberryPi",ip = "192.168.1.100",status = "online",cores = 4))

# 蓝酱整理注释，代码一行没动
