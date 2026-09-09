#字符串的格式化

#拼接
name = '学python'
time = 1
do = 'yyt %s 要加油' %name     #%占位，s将变量变成字符串放入占位的地方

print(do)      #yyt 学python 要加油

do = 'yyt %s %s个月' %(name,time)   #多个变量时要加括号，要按照占位顺序填入，且用逗号分隔

print(do)      #yyt 学python 1个月


name_yyt = 'yyt'
birthday = 2007
year_yyt = 19.5

message = '我叫 %s ,出生于 %d 年, 今年 %.2f 岁了。' %(name_yyt,birthday,year_yyt)
print(message)   #我叫 yyt ,出生于 2007 年, 今年 19.50 岁了。
#%s转变为字符串类型 %d转变为整数 %f转变为浮点类型

message_1 = '今年 %07.2f 岁' %year_yyt
print(message_1)
# 今年  19.50 岁,%m.nf  m表示总长度，n表示小数点后保留的位数,没有指定m时，默认为空格，如果m小于实际长度，则按实际长度输出，m不生效
# %05f时，表示总长度为7位，不够的用0补齐，其他同理


#字符串的方法
s_1 ='hello,world!'

s_2 ='GOOD'

print(s_1.capitalize())    #Hello,world!
print(s_1.title())         #Hello,World!
print(s_1.upper())         #HELLO,WORLD!
print(s_2.lower())         #good


#查找
s_3 = 'hello,china'
print(s_3.find('llo'))     #2
print(s_3.find('llo',3))   #-1,find查找不到值时会返回-1
print(s_3.find('llo',-1,-11))   #-1,因为参数无法反向切片，start无法到达end，取了空值则没有找到llo
print(s_3.find('llo',-10,-1))   #start和end参数表示查找的范围，start表示从第几个开始查找，end表示到第几个结束查找，左闭右开区间
print(s_3.index('llo'))    #2,查找不到值时会报错,参数和find一样
print(s_3.rindex('llo'))   #从末尾开始查找
print(s_3.rfind('llo'))    #2,从右边开始查找
print(s_3.rfind('llo',-10,-1))    #从右边开始查找，在指定范围内
#注意：find和index的区别，find查找不到值时会返回-1，而index查找不到值时会报错,find只能在字符串中查找，不能在列表中查找，而index可以在列表中查找
#注意：rfind和rindex的参数等价于切片


#性质判断
str_1 = 'HellolloeH'
str_2 = 123
print(str_1.startswith('He'))    #True     startswith和endswith判断是否以某个字符串开头和结尾
print(str_1.endswith('l'))       #False
print(str_1.endswith('olloeH'))  #True

#二者判断的长度都是所给出的字符串长度，参数和查找方法同理，区别是会给出布尔值

str_3 = 'abcD1234'
print(str_3.isdigit())      #False   isdigit判断字符串是否为数字，isalpha判断字符串是否为字母，isalnum判断字符串是否为字母和数字
print(str_3.isalpha())      #False
print(str_3.isalnum())      #True


#格式化

str_4 =input('请输入小于20的字符串:')

while len(str_4)>= 20:
    print('请重新输入')
    str_4 = input('请输入小于20的字符串:')

print(str_4.center(20,'*'))          #居中
print(str_4.rjust(20,'^'))           #右对齐
print(str_4.ljust(20,'%'))           #左对齐


#拆分合并
str_5 = 'I Love You'
s1 = str_5.split()
print(s1)       #['I', 'Love', 'You']
s2 = '-'.join(s1)
print(s2)       #I-Love-You
s3 = '123'
print(s3.join(s1))    #I123Love123You,换成元素则用元素连接

print(s2.split('-',1))  #['I', 'Love-You'],split的第二个参数表示分割的次数，默认全部分割


#替换
str_6 = 'Guten Tag'
print(str_6.replace('t','123',1))   #'t'代表要被替换的字符，'123'代表替换后的字符，1代表替换次数


#编码
a = '你行走感到吃力，是因为你在走上坡路'
b = a.encode('UTF-8')
print(type(b))     #<class 'bytes'>
print(b)
print(b.decode('UTF-8'))   #建议在编码时使用UTF-8，解码时也使用UTF-8，避免乱码

c = a.encode('GBK')        
print(c.decode('gbk'))

