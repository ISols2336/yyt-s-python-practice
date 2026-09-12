#知识点：列表方法 append/insert/remove/pop/clear/del/count/index/sort/reverse
#列表是可变的容器，可以增、删、插

languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')  #append：追加到末尾
print(languages)

languages.insert(1,'SQL')  #insert(下标, 值)：在下标 1 处插入
print(languages)

print(languages)         
if 'C++' in languages:       #先判断再删，元素不存在时 remove 会抛 ValueError
    languages.remove('C++')  #remove(值)：删掉第一个等于该值的元素

languages.pop(1)         #pop(下标)：删除指定下标的元素，并返回它
print(languages)         #下标越界会抛 IndexError

items = languages.pop()     #pop() 不写下标 = 删掉最后一个元素，并返回它
print(items)

languages.append(items)     #把刚才删掉的加回去
print(languages)

languages.clear()
print(languages)   #clear：清空内容，列表对象还在，长度为 0

python = ['python','C++'] * 3
python.remove('python')     #remove 只删第一个匹配项
print(python)

del python[0]    #del：直接删除，没有返回值
print(python)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.count('Python'))  #count：统计出现次数
print(items.index('Python',1))  #index(值, 起始下标)：返回第一个匹配的位置
items.sort()
print(items)   #sort：原地排序（默认升序）
items.reverse()  #reverse：原地反转
print(items)

# 蓝酱整理注释，代码一行没动
