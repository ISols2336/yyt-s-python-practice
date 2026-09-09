#列表是一种可变容器，可向列表内增添，删减，插入元素
#列表的方法

languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')  #append可向列表内追加元素
print(languages)

languages.insert(1,'SQL')  #使用insert向列表中插入元素
print(languages)

print(languages)         
if 'C++' in languages:       #可以用列表的remove方法从列表中删除指定元素
    languages.remove('C++')  #如果要删除的元素不在列表内，将引发ValueError错误（值错误）

languages.pop(1)         #还可以使用pop方法删除元素，默认是最后一个元素，可以给一个位置
print(languages)         #如果索引的值超出了范围，会引发IndexError（索引错误）

items = languages.pop()     #pop(n)：删掉下标 n的元素，并且把删掉的元素返回
print(items)                #pop()：删掉最后一个元素，并且把删掉的元素还给你

languages.append(items)     #可以将值重新加入
print(languages)

languages.clear()
print(languages)   #clear方法可以清空列表，但列表本身还存在，调用clear方法后，列表的长度为0

python = ['python','C++'] * 3
python.remove('python')
print(python)

del python[0]    #del关键词后面跟要删除的元素，执行删除且不会返回
print(python)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.count('Python'))  #count可以统计一个元素出现的次数
print(items.index('Python',1))  #index可以查找某个元素在列表中的索引位置，可以选择开始查找的索引位置
                                #只找第一个指定元素出现的位置
items.sort()
print(items)   #sort可以让列表元素排序
items.reverse()  #reverse可以让列表元素反转排序
print(items)