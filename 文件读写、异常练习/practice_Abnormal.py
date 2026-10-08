
#知识点：异常处理全家桶（try / except / else / finally）、自定义异常、raise
#练习：文件打不开会怎样 + 用自定义异常拦住"非法输入"

file = None                  #先设成 None，这样 finally 里能安全地判断"到底开成功没有"

try:
    file = open('三体.txt', 'r', encoding='utf-8')
    
except FileNotFoundError:    #文件不存在
    print('无法打开指定文件！')
except LookupError:          #写了不认识的编码名
    print('指定了未知的编码！')
except UnicodeDecodeError:   #编码对不上，解不开
    print('文件解码发生错误！')
else:                        #★ 没出异常才执行 —— 放"成功之后要做的事"
    print(file.read())
finally:                     #★ 不管成不成功都会执行 —— 放"收尾"的事
    if file:                 #file 有值才关（打不开时它是 None，硬关会报错）
        file.close()

class InputError(ValueError):     #自定义异常：继承 ValueError，所以也能被 except ValueError 抓到
    pass

def fac(num):
    if num < 0:
        raise InputError('只能计算非负整数的阶乘')    #主动抛出，把问题交给调用方去处理
    elif num in (0, 1):
        return 1             #0! 和 1! 都是 1，这是递归的"出口"
    return num * fac(num - 1)   #递归：n! = n × (n-1)!

flag = True
while flag:                  #一直问，直到输入合法
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False         #算成功了才退出循环
    except InputError as err:
        print(err)           #把异常带的提示打出来，然后继续问

# 蓝酱整理注释，代码一行没动
