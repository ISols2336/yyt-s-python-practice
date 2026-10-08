#知识点：类与对象、__init__、self、实例属性、"类.方法(对象)" vs "对象.方法()"、id()
#面向对象入门：定义一个 Coder 类，并对比两种调用方法的方式

class Coder:

    def __init__(self,name,hoay):    #__init__ 是构造方法，创建对象时自动执行
        self.name = name             #self.xxx = 挂在这个对象身上的"属性"
        self.hoay = hoay


    def study(self,lg):              #self 是"哪个对象在调用我"，Python 会自动传进来
        print(f'{self.name}正在学{lg}')

    def play(self):
        print(f'{self.name}正在玩CS')

    def age(self):
        print(f'{self.name}已经{self.hoay}岁了')

cod_1 = Coder('yyt',19)              #创建对象：__init__ 被自动调用
cod_2 = Coder('zjr',19)

coders = [cod_1,cod_2]
print([x for x in coders])           #列表里装的是对象本身（没定义 __repr__ 就打印出对象地址）
print(hex(id(cod_1)))                #id() 取内存地址，hex() 转成十六进制显示

#类.方法  调用方法

Coder.study(cod_1,'python')          #★ 用【类】调用：必须自己把对象当第一个参数传进去

#对象.方法   调用方法

cod_2.play()
cod_2.study('C++')                   #★ 用【对象】调用：self 由 Python 自动补上，不用手写

#类.方法调用一定带上对象
Coder.play(cod_2)

#对象.方法不需要带上对象
cod_1.age()

# 蓝酱整理注释，代码一行没动
