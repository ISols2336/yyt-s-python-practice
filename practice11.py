#知识点：字符串、转义、原始字符串、三元表达式、unicode 编码、切片
#字符串：由零个或多个字符组成的有限序列

s1 = '''hello,
wonderful
world!'''
print(s1)         #三引号定义多行字符串

s2 = '\\hello\\'  #\ 转义：\ 后面的字符不再是它本来的意义
print(s2)
s3 = '\'world\''
print(s3)         #例如 \n 不是字符 \ 和 n，而是换行

#原始字符串：以 r 或 R 开头，字符串里每个字符都是它本来的含义
s4 = '\it \is \time \to \read \now'
s5 = r'\it \is \time \to \read \now'
print(s4)
print(s5)


#字符串比较：逐个比较编码大小，前面都一样时更长的大
s6 = str(input('请输入文本1'))
s7 = str(input('请输入文本2'))

if s6 > s7 :
    print('文本1大')

elif s6 == s7 :
    print('文本12相等')

else :
    print('文本2大')


print('文本1大' if s6 > s7 else '文本12相等' if s6 == s7 else '文本2大')  #三元式：真值 if 条件 else 假值


#字符串的特殊标识：\u 开头是十六进制 unicode 编码
str1 = '\u6211\u7684python\u7ec3\u4e60'
print(str1)  #我的python练习



#字符串的运算
str2 = 'hello' + ',' + 'world'   #+ 拼接
print(str2)

str3 = '!?!' * 3  #* 重复
print(str3)       #!?!!?!!?!

str2 += str3   #+= 原地拼接
print(str2)    #hello,world!?!!?!!?!


#成员运算符 in 和 not in
print('he'not in str2)    #False
print('耍起' in str3)     #False


#获取字符串长度
print(len(str2))     #20


#索引和切片
str4 = 'goodbye,world'
#索引
print(str4[0])   #g

#反向索引
print(str4[-3])  #r


#切片[start:end:step]    step默认是1    取头不取尾
print(str4[::1])     #goodbye,world  省略start从0开始，省略end一直取到末尾
print(str4[::2])     #step 2,gobewrd
print(str4[:2])      #结束位置为2，开始省略，默认为0，结果 go
print(str4[3:])      #dbye,world 从下标 3 一直取到末尾
print(str4[::-2])    #drwebog，step 为负表示反向取

# 蓝酱整理注释，代码一行没动
