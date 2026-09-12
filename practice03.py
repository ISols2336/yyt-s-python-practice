#知识点：赋值、海象、比较、逻辑、成员、身份运算符；== 与 is 的区别；小整数池
a = 15
b = 5
a += b        #a = a + b 的简写；同类还有 -= *= /= //= %=
a *= a + 2    #等价 a = a * (a + 2)，右式整体先算，不是 a = a * a + 2
print(a)  

#海象运算符
print((c:=114)) #:= 赋值的同时返回这个值，常用于循环里省一行
print(c)

#比较运算符：结果都是布尔值 True/False
flag0=1==1              #True
flag1=6>2               #True
flag2=4<1               #False
flag3=1!=3              #True
print('flag0=',flag0)
print('flag1=',flag1)
print('flag2=',flag2)
print('flag3=',flag3)

#逻辑运算符 and / or / not
print(flag0 and flag1)   #True：and 全真才真
print(flag0 and flag2)   #False
print(flag0 or flag2)    #True：or 有真即真
print(not flag3)         #False：not 取反
print(not flag2)         #True


#成员运算符 in / not in：判断元素在不在容器里（字符串/列表/元组/集合/字典）
print('a' in 'abc') #True
print('a' not in 'abc') #False


#身份运算符 is / is not：判断是不是同一个对象（比内存地址，不是比值）
a = 114
b = a

print(id(a))   #id() 返回对象的内存地址（唯一标识）
print(id(b))   #和 id(a) 相同：b 只是 a 的另一个名字，指向同一个对象

print(a is b)  #True   等价于 id(a) == id(b)

print(a is not b)  #False   等价于 id(a) != id(b)



# 小整数池：-5 到 256 的整数被缓存复用，所以是同一个对象
a = 256
b = 256
print(a is b)  #True


# 超过小整数池：本应各自新建对象
y = 258
t = 258
print(y is t) #True：同一个作用域里相同的字面量会被折叠成同一个常量
print(id(y),id(t))

f = 888
g = 777
print(f is g)    #False：值不同
print(id(f),id(g))


item1 = [1,2,3]
item2 = [1,2,3]
print(item1 is item2)   #False：列表内容相同但各自新建，== 为 True、is 为 False

item3 =[3,4,5]
h = item3              #h 不是复制，是指向同一块内存
print(item3 is h)   #True

# 蓝酱整理注释，代码一行没动
