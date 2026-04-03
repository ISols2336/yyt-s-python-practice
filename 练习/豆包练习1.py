#1.输出：Hello, Python
a='Hello'
b='Python'

print(a,',',b)


#2.定义两个变量 c = 10, d = 3
#输出它们的：和、差、积、商、余数

c=10
d=3

print(c+d)
print(c-d)
print(c*d)
print(f'{c/d:.3f}')
print(c%d)


#3.让用户输入身高（米）和体重（千克）
#计算公式：
#BMI = 体重 ÷ (身高 × 身高)
#输出 BMI，保留 2 位小数

BMI=(kg:=float(input('请输入体重'))/(meter:=float(input('请输入身高'))**2))
print(BMI)


#4.让用户输入年龄
#直接输出一句话：
#您今年 X 岁，成年状态：True/False
#成年状态就是：年龄 >= 18 的结果


altjahre=int(input('请输入年龄'))
zhuangtai=bool(altjahre>=18)

print(f'您今年{altjahre:.0f}岁',','f"成年状态:{zhuangtai}")