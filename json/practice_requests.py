#知识点：requests 库、网络接口(API)、status_code、响应转字典、while 计数
#实战：调用一个"随机笑话"接口，只要程序员笑话，凑够 5 条

import requests, time

#先请求一次，看看返回的数据长什么样（有哪些键），方便后面取值
resp = requests.get("https://official-joke-api.appspot.com/random_joke")
resp = resp.json()             #把响应的 JSON 文本解析成字典
print(resp.keys())


i = 1
while i <= 5:
    time.sleep(0.5)            #每次歇半秒——别把人家接口打爆，好习惯
    resp = requests.get("https://official-joke-api.appspot.com/random_joke")
    if resp.status_code == 200:          #200 = 请求成功（不是 200 就别解析了）
        resp = resp.json()
        if resp['type'] == 'programming':        #只要程序员笑话
            print('-'* 50)
            print(f'程序员乐子：{resp['setup']}, id{resp['id']}')
            print('-'* 50)
            i += 1             #★ 只有真打印了才 +1 —— 所以循环会一直转，直到凑够 5 条

# 蓝酱整理注释，代码一行没动
