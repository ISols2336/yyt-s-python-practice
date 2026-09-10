#列表是可变的容器，可以增、删、插
#列表的方法

languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')  #追加到末尾
print(languages)

languages.insert(1,'SQL')  #在下标 1 处插入
print(languages)

print(languages)         
if 'C++' in languages:       #先判断再删，元素不存在时 remove 会抛 ValueError
    languages.remove('C++')

languages.pop(1)         #删除指定下标的元素
print(languages)         #下标越界会抛 IndexError

items = languages.pop()     #pop() 删掉最后一个元素，并把删掉的元素返回
print(items)

languages.append(items)     #把刚才删掉的加回去
print(languages)

languages.clear()
print(languages)   #清空内容，列表对象还在，长度为 0

python = ['python','C++'] * 3
python.remove('python')
print(python)

del python[0]    #del 直接删除，没有返回值
print(python)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.count('Python'))  #统计出现次数
print(items.index('Python',1))  #从下标 1 开始找，只返回第一个匹配的位置
items.sort()
print(items)   #原地排序
items.reverse()  #原地反转
print(items)

# deepseek 酱整理注释，代码一行没动
