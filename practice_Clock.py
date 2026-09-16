#知识点：类 class、对象、self、构造函数 __init__、不变量（% 取余规范化）
#Clock：一个简单的时钟类

class Clock:

    #__init__ 是构造函数：创建对象时自动调用，负责初始化"状态"
    def __init__(self,h = 0,m = 0,s = 0):
        self.hour = h % 24      #% 24 保证小时永远在 0~23（传 24 会变成 0），这就是"不变量"
        self.minute = m % 60    #% 60 保证分钟永远在 0~59
        self.Second = s % 60    #% 60 保证秒永远在 0~59
        #self.xxx = "这个对象自己的属性"，每个对象各存各的，互不干扰

    def run(self,n):
        #run 是"改状态"的方法：让时钟往前走 n 秒
        for i in range(n):
            self.Second += 1

            if self.Second >= 60:      #满 60 秒，进 1 分钟
                self.Second = 0
                self.minute += 1

                if self.minute >= 60:  #满 60 分，进 1 小时
                    self.minute = 0
                    self.hour += 1

                    if self.hour >= 24:    #满 24 小时，归 0
                        self.hour = 0

    def show(self):
        #show 是"读状态"的方法：把当前时间格式化成字符串
        #:0>2 表示"右对齐、用 0 补齐到 2 位"，比如 3 显示成 03
        return f'{self.hour:0>2}:{self.minute:0>2}:{self.Second:0>2}'

day_1 = Clock(h=24,m=0,s=0)   #创建对象：h=24 会被 % 24 规范成 0
day_2 = Clock()                #创建对象：都用默认值 0

day_2.run(40000)               #先"改状态"：让 day_2 走 40000 秒
print(day_2.show())            #再"读状态"：显示结果（11:06:40）

print(day_1.show())            #00:00:00（24 被规范化成 0）

# 蓝酱整理注释，代码一行没动


c1 = Clock(h=23, m=59, s=58)
c1.run(2)
print(c1.show())
# 预期输出：00:00:00


c2 = Clock(h=0, m=0, s=0)
c2.run(40)
print(c2.show())
# 预期输出：00:00:40


c3 = Clock(0,0,55)
c3.run(10)
print(c3.show())
# 预期输出：00:01:05


c4 = Clock(1,59,50)
c4.run(20)
print(c4.show())
# 预期输出：02:00:10


c5 = Clock(10,5,3)
c5.run(86400)
print(c5.show())
# 预期输出：10:05:03


c6 = Clock(0,5,9)
print(c6.show())
# 预期输出：00:05:09
