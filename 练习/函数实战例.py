#知识点：random/string 模块、仅限关键字参数、join、类型注解、素数判断
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

# 蓝酱整理注释，并按你的要求修好了 bug 和建议
