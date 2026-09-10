#赋值运算符
a = 15
b = 5
a += b        # a = a + b
a *= a + 2    # a = a * (a + 2)，不是 a = a * a + 2
print(a)  

#海象运算符
print((c:=114)) #赋值表达式：赋值并返回该值
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
print(flag0 and flag1)   #True：全真才真
print(flag0 and flag2)   #False
print(flag0 or flag2)    #True：有真即真
print(not flag3)         #False：取反
print(not flag2)         #True


#成员运算符  判断元素是否在容器中（字符串、列表、元组、集合、字典等）
print('a' in 'abc') #True
print('a' not in 'abc') #False


#身份运算符  判断两个变量是否引用同一个内存对象
a = 114
b = a

print(id(a))   #id(obj) 返回对象的内存地址
print(id(b))   #和 id(a) 相同：b 只是 a 的另一个名字

print(a is b)  #True   等价于 id(a) == id(b)

print(a is not b)  #False   等价于 id(a) != id(b)



# 小整数池：-5 到 256 范围内的整数复用同一个对象
a = 256
b = 256
print(a is b)  #True


# 超过小整数池：本应各自新建对象
y = 258
t = 258
print(y is t) #True，同一个作用域里相同的字面量会被折叠成同一个常量
print(id(y),id(t))

f = 888
g = 777
print(f is g)    #False
print(id(f),id(g))


item1 = [1,2,3]
item2 = [1,2,3]
print(item1 is item2)   #False：内容相同，但是两个不同的列表对象

item3 =[3,4,5]
h = item3
print(item3 is h)   #True：h 不是新建列表，只是指向 item3 的同一块内存

# deepseek 酱整理注释，代码一行没动
