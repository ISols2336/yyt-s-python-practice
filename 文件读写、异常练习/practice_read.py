#知识点：open/close、readlines、with 自动关文件、os.getcwd
#对比两种开文件的方式：手动 close（容易忘） vs with（推荐）

import os
print("当前目录：", os.getcwd())       #看看程序现在站在哪个目录（相对路径的基准）

#方式一：手动开关
file = open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/致橡树.txt', 'r', encoding='utf-8')

lines = file.readlines()     #一次性读成列表，每个元素是一行（行尾自带 \n）
for line in lines:
    print(line, end='')      #end='' 是因为行里已经带换行了，再自动换行就会空两行

file.close()                 #手动关闭——忘了关，文件会被一直占着


#方式二：with —— 出了这个代码块会自动关闭，不怕忘
with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/test.txt', 'w', encoding='utf-8') as test:
    test.write('\n========测试用文字========')      #'w' 模式：文件不存在就新建，存在就清空重写
    test.write('\n作者:Yyt')
    test.write('\n========随时删除========')

with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/test.txt', 'r', encoding='utf-8') as test:
    print(test.read())       #read() 是整个文件读成一个字符串

# 蓝酱整理注释，代码一行没动
