
#知识点：二进制模式 rb / wb、字节串 b''、用切片"窥探"二进制数据
#练习：把一张图片复制一份，并在末尾追加内容（证明真的写进去了）

#一行里同时开两个文件：file1 读原图，file2 写副本
with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/测试图片.jpg', 'rb') as file1, open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/output.jpg', 'wb') as file2:
    data = file1.read()      #二进制模式读出来的是 bytes（字节串），不是 str
    print(data[::100])       #★ 每 100 个字节取一个 —— 只想看个大概，不想刷屏
    file2.write(data)        #先把原图整个写过去
    file2.write(b'hello,world!')    #★ 再追加一段（b'' 表示字节串）—— 故意"弄坏"它，验证写入生效

with open('C:/Users/Yyt/Desktop/yyt-s-python_practice/文件读写、异常练习/output.jpg', 'rb') as pic:
    data_1 = pic.read()
    print(data_1[-20:])      #看最后 20 个字节 —— 应该能看到刚追加的 hello,world!

# 蓝酱整理注释，代码一行没动
