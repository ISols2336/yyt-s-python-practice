#知识点：json 模块、dumps/dump 与 load 的区别、嵌套结构的序列化
#JSON 练习：字典 → JSON 文本 → 存进文件 → 读回来

import json

my_dict = {

    'name': 'yyt',
    'age': 19,
    'friends': ['何鑫豪', '徐浩钦'],
    'cars': [
        {'brand': '巴伐利亚发动机制造厂', 'max_speed': 250},
        {'brand': '四环素', 'max_speed': 260}
        ]

}

#dumps = 转成"字符串"（多一个 s 就是 string 版）
#注意：默认会把中文转成 \uXXXX，想保留中文可读要加 ensure_ascii=False
print(json.dumps(my_dict))

#dump（不带 s）= 直接写进文件，不用自己转字符串
with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/json/my_dict.json', 'w') as file:
    json.dump(my_dict, file)                   #写入file内

#load（不带 s）= 直接从文件读回来
with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/json/my_dict.json', 'r') as file:
    data = json.load(file)
    print(type(data))          #读回来还是 dict（不是字符串），类型自动还原
    print(data)

# 蓝酱整理注释，代码一行没动
