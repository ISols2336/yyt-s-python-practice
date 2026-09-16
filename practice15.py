#知识点：高阶函数、lambda、map/filter、sorted(key=)、functools.reduce/partial、operator
from typing import Callable   #Callable 是"可调用对象"的类型注解，function 不是真类型

def add(a:int,b:int):
    return a + b


def mul(a:int,b:int):
    return a * b


#calc 是"折叠/reduce"：把 func 依次作用到每个数上，累加或累乘
def calc(start_num:int,func:Callable,*args,**arg):
    res = start_num                    #起点：累加用 0，累乘用 1
    items = list(args) + list(arg.values())   #位置参数 + 关键字参数的值，拼成一个列表
    for item in items:
        if type(item) in (int,float):        #只处理数字，跳过字符串（isinstance 更地道）
            res = func(res,item)             #核心：当前结果和新数字交给 func

    return res

print(calc(1,mul,3,2,3))
print(calc(0, add, 3,2,3))
print(calc(1, mul, 2, 3, 4))
print(calc(0, add, 5, 6, num7=10, num8=20))
print(calc(10, add, 1.5, 2.5, num9=5.0))
print(calc(0, add, 10, "跳过我", 20, name="张三", num10=30))   #字符串被跳过
print(calc(2, mul, 1.5, 4, num_a=2))
#operator.add / operator.mul 是内置的加减乘除函数，from operator import add, mul 后可直接传


#abv：手写的绝对值（Python 内置 abs() 就是它）
def abv(arg):
    if arg <= 0:
        return -arg

    else:
        return arg


#judgment_4：判断是否大于 4（可写成 lambda x: x > 4）
def judgment_4(arg):

    if arg > 4:
        return True

    else:
        return False

data_1 = [1, 5, -2, 8, -4, 10, -7, 3]
data_2 =[-4, 4, -5, 0, -9]
data_3 = [1,2,-3,-1,4]
data_4 = [-100, -20, -3]
data_5 = []                    #空列表，测边界
dataes =[data_1,data_2,data_3,data_4,data_5]

for i in dataes:
    print(list(filter(judgment_4,list(map(abv,i)))))   #map 取绝对值 → filter 留 >4 → list 转列表
    print(list(filter(lambda x:x > 4,list(map(lambda x:-x if x < 0 else x ,i)))))   #同上，改用 lambda 匿名函数
#print(list(filter(lambda x:x > 4,list(map(lambda x:-x if x < 0 else x ,i)))))   #上一行的注释副本

words = ["cat", "banana", "pear", "grapefruit", "dog"]
nums = [5, -2, -9, 7, 1]


def Reverse(a):
    return -len(a)              #返回负长度，配合 sorted 实现"按长度从长到短"排序

sorted_words = sorted(words,key = Reverse)   #key 参数：sorted 会对每个元素先算 key，再按 key 排序
print(sorted_words)
print(sorted(nums,key = abv))   #按绝对值排序


#阶乘：reduce 把 operator.mul 依次作用到 range(2,n+1)，等价于 1*2*3*...*n
import functools
import operator

fac = lambda n: functools.reduce(operator.mul,range(2,n + 1),1)
print(fac(3))


#素数：n>1 且 2~sqrt(n) 里没有一个能整除 n；all 要求所有余数都非 0
is_prime = lambda n: n > 1 and all(map(lambda f: n % f,range(2,int(n ** 0.5) + 1)))
print(is_prime(15))


#偏函数：partial 把函数的某个参数"固定住"，生成一个新函数
int2 = lambda n:functools.partial(int, base = n)   #动态写法：想转几进制传几
int_2 = functools.partial(int,base = 2)            #固定 base=2，二进制转十进制

print(int2(2)('1001'))    #9
print(int_2('1001'))      #9

# 蓝酱整理注释，并把 func 的注解 function 改成了 Callable
