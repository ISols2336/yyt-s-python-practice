#知识点：面向对象进阶——__slots__ 白名单、私有属性(name mangling)、静态方法/类方法、继承与 super()
#面向对象编程进阶
class Student:
    __slots__ = ('__name','__age','sex')            #白名单：只允许这几个属性（省内存、防止写错属性名）

    def __init__(self,name,age):
        self.__name = name      #双下划线开头 = "私有"，Python 会改写成 _Student__name
        self.__age = age

    def doing(self,something):
        print(f'{self.__name}已经{self.__age}岁，正在{something}')

    def __str__(self):
        return f'姓名{self.__name}，年龄{self.__age}，性别{self.sex}'

stu = Student('yyt',19)

stu.doing('python')
#print(stu.__name)      #__name 是私有属性，外部无法访问，双下划线开头


stu.sex = 'man'         #sex 在白名单里，可以正常赋值
print(stu)
#stu.hobby = 'cs'      #不在 __slots__ 白名单里，赋值会报 AttributeError
#print(stu.hobby)


#类方法和静态方法

class Rectangle:
    __slots__ = ('length','width')

    def __init__(self,length,width):
        self.length = length
        self.width = width

    @staticmethod           #静态方法适合校验数据（不需要 self/cls）
    def is_valid(length,width):
        return length > 0 and width > 0

    @classmethod            #类方法的第一个参数是 cls（类本身），常用来当"工厂"造对象
    def create_from_square(cls,side):

        if cls.is_valid(side,side):
            return cls(side,side)   #用 cls(...) 造对象，而不是写死 Rectangle
        else:
            return None

    def perimeter(self):
        return (self.length + self.width)*2

    def area(self):
        return self.length*self.width

    def __str__(self):
        return f'长度{self.length}，宽度{self.width}'

if Rectangle.is_valid(4,5):     #静态方法可以直接用类名调用，不用先造对象
    Re_1 = Rectangle(4,5)
    print(Re_1)
    print(Re_1.perimeter())
    print(Re_1.area())

else:
    print('长度不合法')


# 测试：合法正方形
sq1 = Rectangle.create_from_square(6)
if sq1:
    print(sq1)
    print(f"正方形面积：{sq1.area()}")
else:
    print("正方形边长非法")



#继承：子类自动拥有父类的属性和方法，还能加自己的

class Person:
    __slots__ = ['name','age','sex']

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

    def play(self,game):
        print(f'{self.name}正在玩{game}')

    def sleep(self):
        print('%s正在睡觉' %self.name)

class Student(Person):
    __slots__ = ['studentid']       #子类只写"新增"的属性，父类的槽自动继承（别重复写！）

    def __init__(self, name, age, sex,studentid):
        super().__init__(name, age, sex)    #先让父类初始化它负责的那部分
        self.studentid = studentid

    def study(self,whatclass):
        print(f'{self.name}正在学习{whatclass}')

class Teacher(Person):
    __slots__ = ['teacherid']

    def __init__(self, name, age, sex,teacherid):
        super().__init__(name, age, sex)
        self.teacherid = teacherid


    def teach(self,whatclass):
        print(f'{self.name}正在教授{whatclass}课程')


# ---- 测试继承（蓝酱补的）----
s = Student('小明', 18, '男', '2024001')
t = Teacher('王老师', 35, '女', 'T001')

s.play('篮球')          #继承自 Person
s.study('Python')       #Student 自己的方法
t.sleep()               #继承自 Person
t.teach('数学')         #Teacher 自己的方法

print(isinstance(s, Person))   #True：Student 是 Person 的子类，"小明也是人"
print(s.studentid)             #2024001：子类自己新增的属性

# 蓝酱整理注释，并补了继承部分的测试代码
