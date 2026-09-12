#知识点：字典 dict——键值对；get/keys/values/items/update/pop/popitem/del
#字典：{} 或 dict() 创建，键必须唯一且不可变（常用字符串）

#创建字典
dict_Ras = {

    '型号' : '4B',
    '内存' : '4G',
    '系统' :'Raspberry Pi OS',
    'ip地址':'192.168.1.105',
    '状态':'在线'

}

print(dict_Ras)

#dict 构造器：每一组参数就是一组键值对（键不加引号）
dict_stu = dict(name = '小王' ,age = 18 ,hobby ='写python代码' )
print(dict_stu)               

#zip 把两个序列压成 (键, 值) 对，再转成字典
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
    print(key)           #直接遍历字典，拿到的是键
    print(dict_Ras[key]) #用键取值


#字典的运算

#成员运算符：in 判断的是"键"在不在，不是值
print('内存' in dict_Ras)   #True
print('价格' in dict_Ras)   #False

#索引运算：通过键读写值
print(dict_Ras['型号'])    #4B
dict_Ras['型号'] = 'Pi5'
print(dict_Ras) #{'型号': 'Pi5', '内存': '4G', '系统': 'Raspberry Pi OS', 'ip地址': '192.168.1.105', '状态': '在线'}

#遍历
for _ in dict_Ras :
    print(f'{_}:\t{dict_Ras[_]}')   #\t 是制表符，输出时会对齐

#注意：用索引取值时，键不在字典里会抛 KeyError



#字典的方法：get / keys / values / items

ras_accessory = {

    "主板": "Pi4B 4G",
    "外壳": "亚克力透明壳",
    "散热器": "铝片散热",
    "屏幕": "7寸触摸屏",
    "电池模块": "UPS供电板"
}

#get：安全取值，键不存在时返回 None 或指定默认值，不报错
print(ras_accessory.get('主板'))
print(ras_accessory.get('价格','找不到'))   #第二参数是默认值

#keys
print(ras_accessory.keys())     #所有键

#values
print(ras_accessory.values())   #所有值

#items
print(ras_accessory.items())    #所有键值对，每个是一个元组


for k,v in ras_accessory.items() :
    print(f'{k}:{v}')



#update：合并字典，键相同则覆盖原来的值
# 两个字典拥有同一个键"主板"，值不相同
dict1 = {
    "主板": "Pi4B 4G",
    "外壳": "黑色外壳"
}

dict2 = {
    "主板": "Pi5 8G",   
    "屏幕": "7寸触摸屏"
}
dict1.update(dict2)
print(dict1)     #{'主板': 'Pi5 8G', '外壳': '黑色外壳', '屏幕': '7寸触摸屏'}


#pop：删除指定键并返回值，键不存在会抛 KeyError
print(dict1.pop('主板'))       #Pi5 8G
print(dict1)


#popitem：删除并返回最后一组键值对，字典为空会抛 KeyError
print(dict1.popitem())      #('屏幕', '7寸触摸屏')
print(dict1)


#del关键字：删除指定键值对
del dict1['外壳']
print(dict1)           #键不存在会抛 KeyError

del dict_Ras['系统']
print(dict_Ras)        #{'型号': 'Pi5', '内存': '4G', 'ip地址': '192.168.1.105', '状态': '在线'}

# 蓝酱整理注释，代码一行没动
