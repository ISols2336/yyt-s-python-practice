#元组，是多个元素按照一定顺序构成的序列，元组是不可变类型，这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改
#定义元组通常使用形如(x, y, z)的字面量语法，元组类型支持的运算符跟列表是一样的


t1 = (11,45,14)  #定义一个三元组
t2 = ('先辈',11.4,5,14)   #定义一个四元组

print(type(t1))
print(type(t2))  #查看变量类型

print(len(t1))
print(len(t2))   #查看元组中元素数量

print(t1[0])
print(t2[2])    #索引运算

print(t1[0:2:1])
print(t2[1:3])    #切片运算

for i in t2 :
    print(i)     #遍历元组中的元素

print(11 in t1)  #成员运算符
print('恶臭' in t2)  #False

t3 = t1 + t2   #元组的拼接，因为元组不可变，只能新建
print(t3)

print(t1 == t3)
print(t1 < t3)  #元组的比较
print(t2 == t3)
print(t1 < (45,12))

a = ()  #空元组
print(type(a))   #<class 'tuple'>
b = ('hello')    #字符串
print(type(b))   #<class 'str'>
c = (1,)   #一元组,必须要加括号
print(type(c))   #<class 'tuple'>

#打包和解包
#打包,多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型
tt = 114,514,1919
print(type(tt))    #<class 'tuple'>

#解包,把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
g,h,j = tt
print(g,h,j)   #114 514 1919

#星号表达式
#在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常，错误信息为：too many values to unpack（解包的值太多）或not enough values to unpack（解包的值不足）
tt1 =1,2,3,4,5,6,7
i,o,*p,w = tt1
print(i,o,p,w)    #1 2 [3, 4, 5, 6] 7
#星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素

b,n,m,*k = range(1,10)           #解包语法对所有的序列都成立
print(b,m,n,k)   #1 3 2 [4, 5, 6, 7, 8, 9]

#交换变量的值
v,b,n = 5,6,7
print(v,b,n)    #5 6 7
v,b,n = n,v,b
print(v,b,n)    #7 5 6