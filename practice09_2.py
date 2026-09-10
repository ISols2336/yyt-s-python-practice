#变量运算
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]



print(items1 + items2)     #+ 拼接两个列表

items3 += items2
print(items3)     #[100, 12.3, 'Python', True, 'Python', 'Java', 'Go', 'Kotlin']


print(items1 * 3)   #* 重复列表元素

print(100 in items1)   #in / not in 判断元素在不在列表内
print(100 not in items1)


#操作列表某个元素
items4 = ['CS2',114,514,True,'Java']  #5个元素
print(items4[0])    #索引从 0 开始，取第一个元素
print(items4[4])    #0 到 N-1 是正向索引
#正向索引：N 是元素个数，N-1 是最后一个元素

#反向索引
items4[-1] = 'C++'  #-1 是最后一个元素，可以直接改
print(items4[-1])
print(items4[-5])   #-N 是第一个元素
#索引越界会抛 IndexError: list index out of range


#切片运算
items5 = ['练习',2,'python',True,'gute','努力变好','目标']
#切片语法 [start:end:stride]，左闭右开
print(items5[0:5:3])    #从 0 开始，每次跳 3
print(items5[2:6:3])
print(items5[-1:-6:-2])
print(items5[-1:-5:2])  #start 在 end 右边且 stride 为正，取不到值
print(items5[:3:2])     #start 省略，从 0 开始
print(items5[1::3])     #end 省略，取到末尾
print(items5[3:6])      #stride 省略，默认是 1

#切片也能用来改列表，而且可能改变长度
items5[1:2] = ['practice','C++'] #把下标 1 那一个元素换成两个
print(items5)


#列表的关系运算：从头逐个元素比较
itemsa = [1,2,3,4,5]
itemsb = [1,2,3,4,5]
itemsc = [1,2,3]
itemsd = [True,False]    #True = 1   False = 0
itemse = [0,1]


print(itemsa == itemsb)
print(itemsa != itemsb)
print(itemsa == itemsc)   #前面都相同，元素多的更大
print(itemsd > itemse)    #True 是 1，False 是 0

# deepseek 酱整理注释，代码一行没动
