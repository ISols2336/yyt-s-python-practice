#知识点：% 格式化、字符串方法（查找/判断/对齐/拆分/替换/编码）
#字符串的格式化

#拼接
name = '学python'
time = 1
do = 'yyt %s 要加油' %name     #%s 占位，把变量当字符串填进去

print(do)      #yyt 学python 要加油

do = 'yyt %s %s个月' %(name,time)   #多个变量要加括号，按顺序对应

print(do)      #yyt 学python 1个月


name_yyt = 'yyt'
birthday = 2007
year_yyt = 19.5

message = '我叫 %s ,出生于 %d 年, 今年 %.2f 岁了。' %(name_yyt,birthday,year_yyt)
print(message)   #我叫 yyt ,出生于 2007 年, 今年 19.50 岁了。
#%s 转字符串，%d 转整数，%f 转浮点

message_1 = '今年 %07.2f 岁' %year_yyt
print(message_1)
# %m.nf：m 是总长度，n 是小数点后位数，未指定 m 时默认补空格
# %07.2f 表示总长 7 位，不够的用 0 补齐


#字符串的方法
s_1 ='hello,world!'

s_2 ='GOOD'

print(s_1.capitalize())    #Hello,world!  首字母大写，其余小写
print(s_1.title())         #Hello,World!  每个单词首字母大写
print(s_1.upper())         #HELLO,WORLD!  全大写
print(s_2.lower())         #good          全小写


#查找
s_3 = 'hello,china'
print(s_3.find('llo'))     #2
print(s_3.find('llo',3))   #-1，find 找不到时返回 -1
print(s_3.find('llo',-1,-11))   #-1，start 在 end 右侧，实际取到空范围
print(s_3.find('llo',-10,-1))   #start/end 表示查找范围，左闭右开
print(s_3.index('llo'))    #2，index 找不到时会报错，参数和 find 一样
print(s_3.rindex('llo'))   #从右往左找
print(s_3.rfind('llo'))    #2，从右往左找
print(s_3.rfind('llo',-10,-1))    #在指定范围内从右往左找
#find 找不到返回 -1，index 找不到报错；find 只能用于字符串，index 列表也能用
#rfind / rindex 的 start、end 参数等价于切片


#性质判断
str_1 = 'HellolloeH'
str_2 = 123
print(str_1.startswith('He'))    #True     判断开头
print(str_1.endswith('l'))       #False    判断结尾
print(str_1.endswith('olloeH'))  #True

str_3 = 'abcD1234'
print(str_3.isdigit())      #False   isdigit 判断是否全是数字
print(str_3.isalpha())      #False   isalpha 判断是否全是字母
print(str_3.isalnum())      #True    isalnum 判断是否全是字母或数字


#格式化

str_4 =input('请输入小于20的字符串:')

while len(str_4)>= 20:
    print('请重新输入')
    str_4 = input('请输入小于20的字符串:')

print(str_4.center(20,'*'))          #居中，用 * 补齐到 20 宽
print(str_4.rjust(20,'^'))           #右对齐
print(str_4.ljust(20,'%'))           #左对齐


#拆分合并
str_5 = 'I Love You'
s1 = str_5.split()
print(s1)       #['I', 'Love', 'You']  split 默认按空白拆分
s2 = '-'.join(s1)
print(s2)       #I-Love-You  join 用分隔符连接
s3 = '123'
print(s3.join(s1))    #I123Love123You，用 s3 连接每个元素

print(s2.split('-',1))  #['I', 'Love-You']，第二个参数是分割次数


#替换
str_6 = 'Guten Tag'
print(str_6.replace('t','123',1))   #把 't' 换成 '123'，只换 1 次


#编码：字符串 ↔ 字节
a = '你行走感到吃力，是因为你在走上坡路'
b = a.encode('UTF-8')
print(type(b))     #<class 'bytes'>
print(b)
print(b.decode('UTF-8'))   #编码和解码要用同一种字符集，否则乱码

c = a.encode('GBK')        
print(c.decode('gbk'))

# 蓝酱整理注释，代码一行没动
