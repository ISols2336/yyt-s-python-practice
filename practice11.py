#字符串,由零个或多个字符组成的有限序列

s1 = '''hello,
wonderful
world!'''
print(s1)         #定义多行字符串	

s2 = '\\hello\\'  #可以在字符串中使用\来表示转义，也就是说\后面的字符不再是它原来的意义
print(s2)
s3 = '\'world\''
print(s3)         #例如：\n不是代表字符\和字符n，而是表示换行

#原始字符串,以r或R开头的字符串，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义
s4 = '\it \is \time \to \read \now'
s5 = r'\it \is \time \to \read \now'
print(s4)
print(s5)


#字符串的比较   一个一个比较编码的大小，如果前几个一样，则最长的为大
s6 = str(input('请输入文本1'))
s7 = str(input('请输入文本2'))

if s6 > s7 :
    print('文本1大')

elif s6 == s7 :
    print('文本12相等')

else :
    print('文本2大')


print('文本1大' if s6 > s7 else '文本12相等' if s6 == s7 else '文本2大')  #嵌套三元式


#字符串的特殊标识 可以用八进制和十六进制
str1 = '\u6211\u7684python\u7ec3\u4e60'
print(str1)  #我的python练习



#字符串的运算
str2 = 'hello' + ',' + 'world'   #拼接
print(str2)

str3 = '!?!' * 3  #!?!!?!!?!
print(str3)

str2 += str3   #hello,world!?!!?!!?!
print(str2)


#成员运算符in 和 not in
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
print(str4[:2])      #结束位置为2，开始省略，默认为0go
print(str4[3:])      #dbye,world 从下标一直取到末尾
print(str4[::-2])    #drwebog，省略start取起点，省略end直到方向末尾，step为-2，反向切片