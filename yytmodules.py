#知识点：可变参数 *args / **kwargs、自定义模块、type() 判断类型
#这是我自己写的模块（给别的文件 import 用），放的都是常用工具函数

def add(*args):                     #求数字和函数
    total = 0
    for i in args:                  #args 是个元组，装着所有传进来的参数
        if type(i) in(int,float):   #只累加数字，字符串之类的跳过
            total += i

    return total


def dict(**arg):                    #字典生成函数
    di = arg                        #⚠️ 函数名 dict 把内置的 dict 盖住了（本文件里 dict() 不再是内置类型）
    return di

def dice(n = 5):                    #投骰子函数
    import random
    total = 0
    for _ in range(n):              #_ 表示"这个循环变量我不用"
        total += random.randrange(1,7)      #randrange(1,7) 取 1~6（含头不含尾）

    return total

def factorial_1(y):               #计算阶乘函数
    res = 1
    for x in range(1,y+1):        #从 1 乘到 y；参数故意不叫 x，免得和循环变量撞名
        res *= x
    return res

def f_1():                      #计算组合数函数
    m = int(input('请输入m'))
    n = int(input('请输入n'))

    num = factorial_1(m)//(factorial_1(n)*factorial_1(m-n))    #C(m,n) = m! ÷ (n! × (m-n)!)，// 是整除
    print(num)

# 蓝酱整理注释，代码一行没动
