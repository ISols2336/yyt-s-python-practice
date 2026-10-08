#知识点：抽象基类 ABC、@abstractmethod、多态、isinstance 类型判断
#工资计算程序：不同岗位，同一个方法名，各算各的工资

from abc import ABCMeta, abstractmethod


class Employee(metaclass = ABCMeta):
    #员工：抽象基类——只规定"必须有 get_monthly_salary 这个方法"，自己不实现
    #因为有 abstractmethod，Employee 不能被直接创建，只能被继承

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_monthly_salary(self):
        #抽象方法：只留个空壳，强制每个子类必须自己实现（不实现就报错）
        pass


class Manager(Employee):
    #经理：固定月薪

    def __init__(self, name):
        super().__init__(name)

    def get_monthly_salary(self):
        return 15000.0


class Coder(Employee):
    #程序员：按工时算钱

    def __init__(self, name, work_hour = 0):
        super().__init__(name)
        self.work_hour = work_hour

    def get_monthly_salary(self):
        return 200* self.work_hour      #时薪 200 × 工时


class Salesperson(Employee):
    #销售：底薪 + 提成

    def __init__(self, name, sales = 0):
        super().__init__(name)
        self.sales = sales

    def get_monthly_salary(self):
        return 1800 + self.sales * 0.05   #底薪 1800 + 销售额的 5%


# 多态：同名get_salary方法，不同子类对象执行各自的薪资计算逻辑

Employee_list = [Manager('刘备'), Coder('关羽'), Salesperson('张飞')]

for emp in Employee_list:
    #按"具体是什么类型"补充各自需要的数据
    if isinstance(emp, Coder):
        emp.work_hour = int(input('请输入工作时间'))      #程序员要问工时

    elif isinstance(emp,Salesperson):
        emp.sales = int(input('请输入本月销售额'))         #销售要问销售额

    #这一句就是多态：不管 emp 具体是谁，都用同一个方法名，各算各的
    print(f'名字{emp.name}, 月薪:{emp.get_monthly_salary()}')

# 蓝酱整理注释，代码一行没动
