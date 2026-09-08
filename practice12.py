#数据结构：集合

#无序性：一个集合中，每个元素的地位都是相同的，元素之间是无序的。
#互异性：一个集合中，任何两个元素都是不相同的，即元素在集合中只能出现一次。
#确定性：给定一个集合和一个任意元素，该元素要么属这个集合，要么不属于这个集合，二者必居其一，不允许有模棱两可的情况出现。

#创建集合
set_1 = {1,2,3,4}
print(set_1)

set_2 = set('hello,world')
print(set_2)  #{'r', 'e', 'o', 'h', 'w', ',', 'l', 'd'}  重复的字符只会在集合中出现一次

words = ["apple", "banana", "cat", "dog", "elephant", "ant"]
set_3 = {w.upper() for w in words if len(w) > 3}
print(set_3)          #{'ELEPHANT', 'APPLE', 'BANANA'}

#集合的遍历
for _ in words :
    print(_)


#集合的运算

#成员运算符
set1 = {'python','C++','Java'}
print('Go' in set1)        #False
print('Java' in set1)      #True
print('C++' not in set1)   #False


#二元运算
set2 = {1,2,3,4,5,6,7}
set3 = {2,4,6,8,10}

#交集
print(set2 & set3)            #{2, 4, 6}
print(set3.intersection(set2))

#并集
print(set2 | set3)         #{1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set3.union(set2))

#差集
print(set2 - set3)       #{1, 3, 5, 7}
print(set3 - set2)       #{8, 10}
print(set3.difference(set2))   #{8, 10}

#对称差
print(set2 ^ set3)       #{1, 3, 5, 7, 8, 10}
print(set3.symmetric_difference(set2))      #{1, 3, 5, 7, 8, 10}
res = set3.symmetric_difference_update(set2)     #update方法会直接修改原集合，返回值为None
print(res,set3)        #None {1, 3, 5, 7, 8, 10}

#也可以在运算符后加上等号，表示将结果赋值给左边的集合
#set2 &= set3



#集合的比较

set4 = {1,3,5}
set5 = {1,3,5,7,9}
set6 = {1,3,5,7,9}

print(set4 < set5)    #True    判断set4是否为set5的真子集，反过来判断set5是否为set4的超集
print(set4 <= set5)   #True    判断set4是否为set5的子集
print(set6 < set5)    #False    

print(set4.issubset(set5))     #issubset判断set4是否为set5的子集       True
print(set5.issuperset(set4))   #issuperset判断set5是否为set4的超集     True


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


set_4.remove(rm_1)      #remove方法删除指定元素，如果元素不存在则会报错

print(f'删除后的集合结果为:{set_4}')


#清空元素
et1 = {67,114,514}
et1.clear()
print(et1)       #set()

#isdisjoint()方法判断两个集合是否有交集，如果没有交集则返回True，否则返回False
set7 = {'Niko','m0NESY','kuyousuke'}
set8 = {'Donk','Shiro','kuyousuke'}

print(set7.isdisjoint(set8))    #False


#不可变集合
fset1 = frozenset({1,2,3,4})
fest2 = frozenset(range(7))

print(fset1)
print(fest2)
#frozenset不支持添加和删除元素