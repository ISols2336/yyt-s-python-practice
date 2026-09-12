#知识点：集合 set——无序、不重复；交/并/差/对称差；frozenset 不可变
#数据结构：集合
#无序性：元素之间没有顺序。
#互异性：元素不能重复，重复的会自动去重。
#确定性：一个元素要么属于这个集合，要么不属于。

#创建集合：{} 或 set()
set_1 = {1,2,3,4}
print(set_1)

set_2 = set('hello,world')      #set(可迭代对象) 会拆成单个字符
print(set_2)  #{'r', 'e', 'o', 'h', 'w', ',', 'l', 'd'}  重复的字符只出现一次

words = ["apple", "banana", "cat", "dog", "elephant", "ant"]
set_3 = {w.upper() for w in words if len(w) > 3}   #集合生成式
print(set_3)          #{'ELEPHANT', 'APPLE', 'BANANA'}

#集合的遍历
for _ in words :
    print(_)


#集合的运算

#成员运算符：比列表快，因为集合靠哈希查找
set1 = {'python','C++','Java'}
print('Go' in set1)        #False
print('Java' in set1)      #True
print('C++' not in set1)   #False


#二元运算
set2 = {1,2,3,4,5,6,7}
set3 = {2,4,6,8,10}

#交集：两个都有的
print(set2 & set3)            #{2, 4, 6}
print(set3.intersection(set2))

#并集：合在一起
print(set2 | set3)         #{1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set3.union(set2))

#差集：只在前一个里
print(set2 - set3)       #{1, 3, 5, 7}
print(set3 - set2)       #{8, 10}
print(set3.difference(set2))   #{8, 10}

#对称差：只在一方里，去掉共同部分
print(set2 ^ set3)       #{1, 3, 5, 7, 8, 10}
print(set3.symmetric_difference(set2))      #{1, 3, 5, 7, 8, 10}
res = set3.symmetric_difference_update(set2)     #注意：带 update 的版本会直接改原集合，返回 None
print(res,set3)        #None {1, 3, 5, 7, 8, 10}

#运算符后面加等号，表示把结果赋给左边的集合
#set2 &= set3



#集合的比较：子集 / 超集

set4 = {1,3,5}
set5 = {1,3,5,7,9}
set6 = {1,3,5,7,9}

print(set4 < set5)    #True    真子集：被包含且不相等
print(set4 <= set5)   #True    子集：被包含（可以相等）
print(set6 < set5)    #False

print(set4.issubset(set5))     #issubset：set4 是 set5 的子集       True
print(set5.issuperset(set4))   #issuperset：set5 是 set4 的超集     True


#集合的方法

set_4 = {1,20,300}

#添加元素
set_4.add(4000)
print(set_4)

#删除元素
print(f'现在集合内有{set_4}')
rm_1 = int(input('选择你要删除的元素:'))

while rm_1 not in set_4:
    rm_1 = int(input('请重新输入正确的元素:'))


set_4.remove(rm_1)      #remove 删除指定元素，元素不存在时会报错

print(f'删除后的集合结果为:{set_4}')


#清空元素
et1 = {67,114,514}
et1.clear()
print(et1)       #set()

#isdisjoint()：两个集合没有交集时返回 True
set7 = {'Niko','m0NESY','kuyousuke'}
set8 = {'Donk','Shiro','kuyousuke'}

print(set7.isdisjoint(set8))    #False


#不可变集合：frozenset，创建后不能增删改
fset1 = frozenset({1,2,3,4})
fest2 = frozenset(range(7))

print(fset1)
print(fest2)
#frozenset不支持添加和删除元素

# 蓝酱整理注释，代码一行没动
