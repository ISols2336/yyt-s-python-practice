#元组：多个元素按顺序构成的序列
#元组是不可变类型：一旦定义，元素不能增删，元素的值也不能改
#定义用 (x, y, z) 字面量，支持的运算符和列表一样


t1 = (11,45,14)  #三元组
t2 = ('先辈',11.4,5,14)   #四元组

print(type(t1))
print(type(t2))  #都是 <class 'tuple'>

print(len(t1))
print(len(t2))   #元素个数

print(t1[0])
print(t2[2])    #索引

print(t1[0:2:1])
print(t2[1:3])    #切片

for i in t2 :
    print(i)     #遍历

print(11 in t1)  #成员运算
print('恶臭' in t2)  #False

t3 = t1 + t2   #拼接会新建元组，原元组不变
print(t3)

print(t1 == t3)
print(t1 < t3)  #比较
print(t2 == t3)
print(t1 < (45,12))

a = ()  #空元组
print(type(a))   #<class 'tuple'>
b = ('hello')    #没有逗号，这是字符串
print(type(b))   #<class 'str'>
c = (1,)   #一元组必须加逗号
print(type(c))   #<class 'tuple'>

#打包和解包
#打包：多个逗号分隔的值赋给一个变量，会打包成元组
tt = 114,514,1919
print(type(tt))    #<class 'tuple'>

#解包：元组赋给多个变量，会拆开分别赋值
g,h,j = tt
print(g,h,j)   #114 514 1919

#星号表达式
#解包时元素个数和变量个数不匹配会抛 ValueError：
#too many values to unpack / not enough values to unpack
tt1 =1,2,3,4,5,6,7
i,o,*p,w = tt1
print(i,o,p,w)    #1 2 [3, 4, 5, 6] 7
#带星号的变量会变成列表，可以装 0 个或多个元素

b,n,m,*k = range(1,10)           #解包对任何序列都成立
print(b,m,n,k)   #1 3 2 [4, 5, 6, 7, 8, 9]

#交换变量的值
v,b,n = 5,6,7
print(v,b,n)    #5 6 7
v,b,n = n,v,b
print(v,b,n)    #7 5 6

# deepseek 酱整理注释，代码一行没动
