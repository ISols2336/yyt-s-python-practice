import time           #import是用来导入模块的，time是一个内置模块，提供了各种时间相关的函数和类。

print('hello, world')
time.sleep(1)         #time模块中的sleep函数可以让程序暂停一段时间，参数是暂停的秒数，这里暂停1秒



#for-in循环
import time

for i in range(30):        #range用来生成整数序列数个数，从0开始,到结束数字前一个数结束，循环30次
    print('hello, world')  #for后必须加临时变量，可以用也可以不用，不用也可以用_表示这个变量不用
    time.sleep(1)          #range也可以range（1，100）1到99，取不到100，也可以range（1，100，2）2表示步长，递增2


#用for-in算1到100的和

total = 0
for H in range(1,101):
    total =total + H      #也可以使用简写total += H，意思是total = total + H
                          #偷懒写法，举例total *= 2，意思是total = total * 2，total /= 2，意思是total = total / 2，total -= 2，意思是total = total - 2  

print(total)


#也可以使用sum函数
print(sum(range(1,101)))  #sum函数可以对一个可迭代对象进行求和，range(1,101)生成一个从1到100的整数序列，sum函数对这个序列进行求和，得到1到100的和
print(sum([1,100]))       #sum函数也可以对一个列表进行求和


#while循环，后续条件为Ture就一直执行，直到条件Flase停止
#使用while循环算1到100的和
t = 0
i = 1

while i <= 100 :
    t += i
    i += 1

print(t)


#也可以使用break关键字，立刻结束循环
while True :
    t += i
    i += 1
    if i > 100 :
        break
print(t)


#也可以用continue关键字，跳过这一次，继续循环
#从1到100的偶数求和
total_1 = 0

for ou in range(1,101):
    if ou % 2 != 0:
        continue
    total_1 += ou

print(total_1)



#练习，判断用户输入的数是否为素数

nummer = int(input('请输入一个大于1的数字'))
nummer05 = int(nummer**0.5)

if nummer <= 1 :
    print('请输入正确的数字')

is_ = True

for s in range(2,nummer05 + 1):
    if nummer % s == 0:
       is_ = False
       break


if is_ == False:
    print(f'{nummer}不是素数')

else :
    print(f'{nummer}是素数')