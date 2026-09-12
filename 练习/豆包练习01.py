#知识点：算术运算、除法保留小数、海象运算符 :=、bool 转换
#1.输出：Hello, Python
a='Hello'
b='Python'

print(a,',',b)       #print 多个参数默认用空格分隔，',' 是单独一个参数


#2.定义两个变量 c = 10, d = 3
#输出它们的：和、差、积、商、余数

c=10
d=3

print(c+d)           #和 13
print(c-d)           #差 7
print(c*d)           #积 30
print(f'{c/d:.3f}')  #商，保留 3 位小数（3.333）
print(c%d)           #余数 1，% 取余


#3.让用户输入身高（米）和体重（千克）
#BMI = 体重 ÷ (身高 × 身高)，保留 2 位小数

BMI=(kg:=float(input('请输入体重'))/(meter:=float(input('请输入身高'))**2))
print(BMI)


#4.让用户输入年龄
#输出：您今年 X 岁，成年状态：True/False（成年即年龄 >= 18）


altjahre=int(input('请输入年龄'))
zhuangtai=bool(altjahre>=18)     #比较结果本来就是布尔，bool() 可省略

print(f'您今年{altjahre:.0f}岁',','f"成年状态:{zhuangtai}")

# 蓝酱整理注释，代码一行没动
