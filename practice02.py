#知识点：类型转换 float/int/bool/str，字符与编码互换 chr/ord
a=100
b=114.514
c='我的python练习'
d=''                   #空字符串，长度为 0
e='d'
f=12

print(float(a))        #100.0：整数 → 浮点数

print(int(b))          #114：int() 截断取整，不是四舍五入

print(bool(c))         #True：非空字符串为真（空串、0、None 才是 False）

print(bool(d))         #False：空字符串转布尔为 False

print(chr(a))          #d：chr(编码)→字符；ord(字符)→编码，两者互为反操作

print(ord(e))          #100：'d' 的 ASCII 码是 100

print(str(f),'天')     #数字转成字符串，才能和 '天' 拼在一起输出

# 蓝酱整理注释，代码一行没动
