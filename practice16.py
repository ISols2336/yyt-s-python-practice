#知识点：装饰器、闭包、@ 语法糖、functools.wraps、递归、lru_cache 缓存
import time
import random

def download(filename):
    print(f'开始下载文件{filename}')
    time.sleep(random.random() * 5)
    print(f'文件{filename}下载完成')


def upload(filename):
    print(f'开始上传文件{filename}')
    time.sleep(random.random() * 6)
    print(f'文件{filename}上传完成')

download('豆包老师')
upload('蓝酱小可爱')

#加入显示用时功能：手写计时
start = time.time()
download('蓝酱小可爱')
end = time.time()
print(f'下载文件花费{end - start:-^6.2f}秒')   #-^6.2f：居中、用 - 填充到宽 6、保留 2 位

start = time.time()
upload('豆包老师')
end = time.time()
print(f'上传文件花费{end - start:*>8.2f}秒')   #*>8.2f：右对齐、用 * 填充到宽 8
#过于重复 → 引出装饰器


##装饰器函数：给函数"套壳"加功能，不改原函数本身
from functools import wraps


def record_time(func):

    #@wraps(func)：让 wrapper 伪装成原函数，保留 __name__ 等元信息
    @wraps(func)
    def wrapper(*args,**kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        res = func(*args,**kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'操作文件花费{end - start:.2f}秒')
        # 返回被装饰函数的返回值
        return res

    return wrapper

wra = record_time(download)     #手动版：拿变量接收返回的 wrapper
wra('豆包老师')


##装饰器的本质（五步）：
##1. 装饰器接收「原函数」作为参数；
##2. 在内部定义包装函数 wrapper；
##3. wrapper 里调用原函数（原函数逻辑不变，作为内核）；
##4. 在调用原函数之前/之后，可以塞额外代码（计时、日志等）；
##5. 最后把这个 wrapper 返回，用变量接住再调用，就会执行「前置 → 原函数 → 后置」。


#语法糖：@record_time 等价于 download = record_time(download)

@record_time
def download(filename):
    print(f'开始下载文件{filename}')
    time.sleep(random.random() * 5)
    print(f'文件{filename}下载完成')

@record_time
def upload(filename):
    print(f'开始上传文件{filename}')
    time.sleep(random.random() * 6)
    print(f'文件{filename}上传完成')

download('蓝酱.ai')
upload('豆包.ai')


#加了 @wraps，两个函数都能保留自己的原名（若不加，都会变成 "wrapper"）
print(download.__name__)   #download
print(upload.__name__)     #upload


#递归：函数自己调用自己；必须有"基线条件"（终止条件），否则无限递归

def fac(num:int):
    if num in (0,1):          #基线条件：0 和 1 的阶乘都是 1
        return 1

    return num * fac(num - 1)   #递归：n! = n × (n-1)!

print(fac(5))   #120


#斐波那契数列：1,1,2,3,5,8,...（后一项 = 前两项之和）
def fib(num:int):
    if 0 < num <= 2 :          #基线条件：第 1、2 项都是 1
        return 1

    return fib(num - 1) + fib(num - 2 )   #递归：fib(n) = fib(n-1) + fib(n-2)

print(fib(6))   #8

#有效率的写法：循环 + 元组交换，O(n)；上面的递归是 O(2^n)，n 一大就慢到爆
def fib_2(num:int):
    a,b = 0,1
    for _ in range(num):
        a , b = b , a + b      #a 往前走一步，b 变成 a+b

    return a

print(fib_2(60))   #1548008755920，秒出

#语法糖：lru_cache 给递归加"记忆"，算过的结果存起来，避免重复计算
from functools import lru_cache

@lru_cache()                  #lru_cache 是缓存装饰器，把递归从 O(2^n) 变成 O(n)
def fib(num:int):
    if 0 < num <= 2 :
        return 1

    return fib(num - 1) + fib(num - 2 )


print(fib(60))   #1548008755920，加了缓存后秒出

# 蓝酱整理注释：新增了递归和 lru_cache 的知识点注释
