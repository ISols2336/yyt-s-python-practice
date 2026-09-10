#字典


#创建字典
dict_Ras = {

    '型号' : '4B',
    '内存' : '4G',
    '系统' :'Raspberry Pi OS',
    'ip地址':'192.168.1.105',
    '状态':'在线'

}

print(dict_Ras)

#dict 构造器：每一组参数就是一组键值对
dict_stu = dict(name = '小王' ,age = 18 ,hobby ='写python代码' )
print(dict_stu)               

#用 zip 压缩两个序列再创建字典
dict_ran = dict(zip('ABCDEFG',range(7)))
print(dict_ran)

# 字典生成式
products = ["GPW鼠标", "棱镜耳机", "机械键盘", "鼠标垫"]
stock = [12, 8, 25, 3]

dict_1 = {products[x]: stock[x] for x in range(len(stock)) if stock[x] < 10 }    #k:v 形式，带条件筛选
print(dict_1)


#键值对
print(len(dict_Ras))    #5
for key in dict_Ras:
    print(key)           #直接遍历只能拿到键，值要用键去取
    print(dict_Ras[key])


#字典的运算

#成员运算符
print('内存' in dict_Ras)   #True     判断的是键，不是值
print('价格' in dict_Ras)   #False

#索引运算
print(dict_Ras['型号'])    #4B
dict_Ras['型号'] = 'Pi5'
print(dict_Ras) #{'型号': 'Pi5', '内存': '4G', '系统': 'Raspberry Pi OS', 'ip地址': '192.168.1.105', '状态': '在线'}

#遍历
for _ in dict_Ras :
    print(f'{_}:\t{dict_Ras[_]}')   #\t 是制表符，输出时会对齐

#注意：用索引取值时，键不在字典里会抛 KeyError



#字符串的方法

ras_accessory = {

    "主板": "Pi4B 4G",
    "外壳": "亚克力透明壳",
    "散热器": "铝片散热",
    "屏幕": "7寸触摸屏",
    "电池模块": "UPS供电板"
}

#get
print(ras_accessory.get('主板'))   #get 取值，键不存在时返回 None
print(ras_accessory.get('价格','找不到'))   #也可以指定默认值

#keys
print(ras_accessory.keys())     #所有键

#values
print(ras_accessory.values())   #所有值

#items
print(ras_accessory.items())    #所有键值对，每个键值对是一个元组


for k,v in ras_accessory.items() :
    print(f'{k}:{v}')



#update
# 两个字典拥有同一个键"主板"，值不相同
dict1 = {
    "主板": "Pi4B 4G",
    "外壳": "黑色外壳"
}

dict2 = {
    "主板": "Pi5 8G",   
    "屏幕": "7寸触摸屏"
}
dict1.update(dict2) #把 dict2 合并进 dict1，键相同则覆盖原来的值
print(dict1)     #{'主板': 'Pi5 8G', '外壳': '黑色外壳', '屏幕': '7寸触摸屏'}


#pop
print(dict1.pop('主板'))       #Pi5 8G
print(dict1)     #pop 删除指定键并返回值，键不存在会抛 KeyError


#popitem
print(dict1.popitem())      #('屏幕', '7寸触摸屏')
print(dict1)                #popitem 删除并返回最后一组键值对，字典为空会抛 KeyError


#del关键字
del dict1['外壳']      #删除指定键值对
print(dict1)           #键不存在会抛 KeyError

del dict_Ras['系统']
print(dict_Ras)        #{'型号': 'Pi5', '内存': '4G', 'ip地址': '192.168.1.105', '状态': '在线'}

# deepseek 酱整理注释，代码一行没动
