#知识点：random/string 模块、仅限关键字参数、join、类型注解、素数判断、统计（极差/均值/中位数/方差/标准差/变异系数）、双色球抽奖（random.sample）
#随机验证码函数
import random
import string

#string.digits 是 '0~9'，string.ascii_letters 是 'a~zA~Z'，拼起来就是验证码字符池
ALL_CHARS= string.digits + string.ascii_letters

def generate_code(* , code_len = 4):
    #* 后面的参数是「仅限关键字」：调用时只能写 code_len=7，不能位置传参
    if code_len <= 0:
        return '请输入大于0的正数'
        
    elif isinstance(code_len, float):   #isinstance 比 type(x) is float 更地道，还能识别子类
        return '请输入整数'

    #random.choices(字符池, k=长度)：从池子里随机挑 k 个字符；join 拼成字符串
    return ''.join(random.choices(ALL_CHARS,k = code_len))


for i in range(5):      #连抽 5 个验证码看看
    print(generate_code( code_len = 7))



#素数判断函数

def is_prime(num:int):      #num:int 是类型注解，提示参数该传整数
    count = 0               #因数计数器：原来用列表 append 计数，改成整数更直观
    for i in range(1,num + 1):
        if num % i == 0 :   #% 取余，余 0 表示 i 能整除 num
            count += 1

    return count == 2       #素数=恰有 1 和它本身两个因数；直接返回布尔值更通用


print(is_prime(6))          #False


def is_prime_1(num:int):

    #优化版：只试除到平方根，能整除就说明有别的因数，立刻判定不是素数
    if num <= 1:            #1、0、负数都不是素数；没有这行，num=1 会漏判成素数
        return False

    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True


print(is_prime_1(1))        #False，已修好
print(is_prime_1(7))        #True，7 是素数



#最大公约数：辗转相除法（欧几里得算法）
def GCD(num_1:int,num_2:int):
    if num_2 == 0:          #边界：gcd(a, 0) = a，先拦掉避免后面除以 0
        return num_1

    while num_1 % num_2 != 0:
        num_1,num_2 = num_2,num_1 % num_2   #元组交换：余数当新除数，直到整除

    return num_2

print(GCD(12,18))   #6


def LCM(num_1:int,num_2:int):
    return num_1 * num_2 // GCD(num_1,num_2)   #最小公倍数 = 两数之积 ÷ 最大公约数

print(LCM(12,18))   #36



#极差：最大值减最小值
def ptp(*nums):
    return max(nums) - min(nums)

print(ptp(3,9,1,7))   #8

#均值：总和除以个数
def mean(*nums):
    res = 0
    for i in nums:
        res += i
    return res/len(nums)

print(mean(1,2,3,4))   #2.5

#中位数：先排序，奇数个取中间，偶数个取中间两个的平均
def median(*nums):
    res = sorted(nums)          #sorted 返回排好序的新列表，原数据不变
    res_len = len(res)
    if res_len % 2 != 0:        #奇数个
        return res[res_len//2]  #// 整除，正好是中间下标
    else:                       #偶数个
        return mean(res[res_len//2 - 1] , res[res_len//2])

print(median(1,3,2,4,5))   #3
print(median(1,2,3,4))     #2.5


#样本方差：衡量数据离平均值的平均远近（样本版，除以 n-1）
def var_1(*data):
    res = mean(*data)          #先算平均值，复用上面的 mean
    res_list = []              #存每个数到平均值的距离的平方
    for i in data:
        res_list.append((i - res) ** 2)   #(每个数 - 平均)²

    return sum(res_list) / (len(data) - 1)   #除以 n-1 是样本方差（除以 n 是总体方差）

print(var_1(3, 5, 7))   #4.0


#标准差：方差的平方根，和原数据同单位，波动大小更直观
def std(*data):
    return var_1(*data) ** 0.5   #** 0.5 就是开平方

print(std(3,5,7))   #2.0


#变异系数：标准差 ÷ 平均值，去掉单位的"相对"波动指标
def cv(*data):
    return std(*data) / mean(*data)

print(cv(3,5,7))   #0.4


#双色球随机选号：红球 6 个（1~33，不重复）+ 蓝球 1 个（1~16）
import random

RED_ball = [i for i in range(1,34)]     #红球 1~33（列表生成式，34 取不到）
BLUE_ball = [i for i in range(1,17)]    #蓝球 1~16

def choose():
    res = random.sample(RED_ball,6)  #sample 无放回抽取：6 个红球不重复（用 choice 会抽到重复的）
    res.sort()                        #升序排好，方便看
    res.append(random.choice(BLUE_ball))  #蓝球是单独抽的，用 choice 随机选 1 个
    return res                        #返回 [6个红球..., 1个蓝球]

def display(a:int):                    #a:int 类型注解，表示抽几注
    for _ in range(a):                 #连抽 a 注
        ticks = choose()
        red = ticks[:-1]               #切片：除最后一个是红球
        blue = ticks[-1]               #最后一个是蓝球
        red_str = ' '.join(f'{num}' for num in red)   #生成器表达式：数字拼成字符串
        print(f'\n红球{red_str} | 蓝球{blue}')

display(3)

# 蓝酱整理注释，代码一行没动
