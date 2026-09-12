import time           #time：内置模块，time.sleep(n) 让程序暂停 n 秒

print('hello, world')
time.sleep(1)         #暂停 1 秒



#知识点：for-in 循环 + range；range(起, 止, 步长)，左闭右开
import time

for i in range(30):        #range(30)：0 到 29，共 30 次
    print('hello, world')
    time.sleep(1)          #range(1,100) 是 1 到 99；range(1,100,2) 步长为 2


#用for-in算1到100的和

total = 0
for H in range(1,101):
    total =total + H      #等价于 total += H（累加）

print(total)


#也可以使用sum函数
print(sum(range(1,101)))  #sum 对可迭代对象求和，一行顶上面五行的活
print(sum([1,100]))       #也可以对列表求和


#知识点：while 循环；break 立刻退出，continue 跳过本次
#使用while循环算1到100的和
t = 0
i = 1

while i <= 100 :
    t += i
    i += 1               #忘了这行会死循环

print(t)


#break：立刻结束整个循环
while True :
    t += i
    i += 1
    if i > 100 :
        break
print(t)


#continue：跳过这一次，继续下一次循环
#从1到100的偶数求和
total_1 = 0

for ou in range(1,101):
    if ou % 2 != 0:      #奇数就跳过
        continue
    total_1 += ou

print(total_1)



#练习，判断用户输入的数是否为素数
#素数：只有 1 和它本身两个因数；试除到平方根即可
nummer = int(input('请输入一个大于1的数字'))
nummer05 = int(nummer**0.5)      #只需试除到平方根，减少循环次数

if nummer <= 1 :
    print('请输入正确的数字')

is_ = True              #先假设是素数

for s in range(2,nummer05 + 1):
    if nummer % s == 0:     #被整除了，说明不是素数
       is_ = False
       break


if is_ == False:
    print(f'{nummer}不是素数')

else :
    print(f'{nummer}是素数')     #累死我了

# 蓝酱整理注释，代码一行没动
