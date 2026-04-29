#赋值运算符
a = 15
b = 5
a += b        # 相当于：a = a + b
a *= a + 2    # 相当于：a = a * (a + 2)
print(a)  

#海象运算符
print((c:=114)) #将右侧的值赋给左边变量
print(c)

#比较运算符和逻辑运算符and,or,not

#比较运算符
flag0=1==1              #True
flag1=6>2               #True
flag2=4<1               #False
flag3=1!=3              #True
print('flag0=',flag0)
print('flag1=',flag1)
print('flag2=',flag2)
print('flag3=',flag3)

#逻辑运算符and,not,or
print(flag0 and flag1)   #只要有一个False就是False
print(flag0 and flag2)
print(flag0 or flag2)    #只要有一个True就是True
print(not flag3)         #与值反着输出
print(not flag2)


#成员运算符  用于判断一个元素是否存在于某个序列 / 容器中（字符串、列表、元组、集合、字典等）
print('a' in 'abc') #True
#判断元素是否在序列中
print('a' not in 'abc') #False
#判断元素是否不在序列中


#身份运算符  用于判断两个变量是否引用[同一个内存对象]的运算符
a = 114
b = a

print(id(a))   #每个 Python 对象在内存中都有唯一的地址，id(obj) 会返回这个地址的整数表示
print(id(b))

print(a is b)  #True    
#is判断两个变量是否指向同一个内存对象	等价于id(a) == id(b)

print(a is not b)  #False
#is not判断两个变量是否指向不同的内存对象	等价于id(a) != id(b)



# 小整数池内：复用同一个对象（-5 —— 256）
a = 256
b = 256
print(a is b)  #True


# 超过小整数池：赋值新建对象
y = 258
t = 258
print(y is t) #复用一个对象会优化折叠，内存地址相同，输出True
print(id(y),id(t))

f = 888
g = 777
print(f is g)    #False
print(id(f),id(g))


item1 = [1,2,3]
item2 = [1,2,3]
print(item1 is item2)   #False
#列表哪怕内容相同，但是新建列表的内存地址不相同，所以会输出False

item3 =[3,4,5]
h = item3
print(item3 is h)   #不是新建列表,只是把h指向item3的同一块内存
#True