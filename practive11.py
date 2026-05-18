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

s6 = str(input('请输入文本1'))
s7 = str(input('请输入文本2'))

if s6 > s7 :
    print('文本1大')

elif s6 == s7 :
    print('文本12相等')

else :
    print('文本2大')


print('文本1大' if s6 > s7 else '文本12相等' if s6 == s7 else '文本2大')  #三元式