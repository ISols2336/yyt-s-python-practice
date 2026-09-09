#变量运算
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]      



print(items1 + items2)     #也可以使用+运算符，完成两个列表的拼接拼接运算会将两个列表中的元素连接起来放到一个列表中

items3 += items2
print(items3)     #[100, 12.3, 'Python', True, 'Python', 'Java', 'Go', 'Kotlin']


print(items1 * 3)   #可以使用*运算符实现列表的重复运算，*运算符会将列表元素重复指定的次数

print(100 in items1)   #可以使用成员运算符in ，not in判断一个元素在不在列表内
print(100 not in items1)


#操作列表某个元素
items4 = ['CS2',114,514,True,'Java']  #5个元素
print(items4[0])    #可以使用[]运算符，指定元素位置访问该元素，0访问列表中的第一个元素
print(items4[4])    #称为索引运算，元素位置可以是0到N-1的整数，也可以是-1到-N的整数，分别为正向索引和反向索引
#正向索引，N代表列表元素内元素个数，N-1访问列表中最后一个元素

#反向索引
items4[-1] = 'C++'  #访问后，可以改变列表内元素
print(items4[-1])   #[-1]可以访问列表中的最后一个元素
print(items4[-5])   #[-N]可以访问第一个元素
#要避免索引越界错误，访问列表元素时，索引必须在有效范围内，否则会抛出IndexError异常
#list index out of range，翻译成中文就是“数组索引超出范围”


#切片运算
items5 = ['练习',2,'python',True,'gute','努力变好','目标']
#切片运算是形如[start:end:stride]的运算符,分别是：起始位置，终止位置，跨度
print(items5[0:5:3])    #第一个元素在start，第二个元素在start + stride位置（start + stride < end）
print(items5[2:6:3])
print(items5[-1:-6:-2])
print(items5[-1:-5:2])  #反向索引，跨度为正，无作用
print(items5[:3:2])     #start为0时，可以省略
print(items5[1::3])     #end为N时，可以省略
print(items5[3:6])     #stride为1时，可以省略

#还可以通过切片操作修改列表中的元素
items5[1:2] = ['practice','C++'] #切片是左闭右开，[1:2]相当于将2挖掉了替换成了想要替换的元素，可能会增多
print(items5)


#列表之间还可以进行关系运算
itemsa = [1,2,3,4,5]
itemsb = [1,2,3,4,5]
itemsc = [1,2,3]
itemsd = [True,False]    #True = 1   False = 0
itemse = [0,1]


print(itemsa == itemsb)
print(itemsa != itemsb)   #比较时，先从列表第一个开始比较，如果相同就继续比较下一个元素
print(itemsa == itemsc)   #如果前面都相同，那看个数元素多的列表为大
print(itemsd > itemse)    #True是1，False是0