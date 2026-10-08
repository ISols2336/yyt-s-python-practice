#知识点：函数封装、sum/len 算平均、round 四舍五入、多分支 if-elif-else
#成绩单作业：算平均分 + 按分数划等级

def average(scores):
    #算平均分，保留 1 位小数
    res = sum(scores)/len(scores)      #sum 求和，len 取个数
    res = round(res,1)                 #round(数, 位数) → 四舍五入到 1 位小数
    return res


def grade(score):
    #按分数划等级：90+ → A，80+ → B，70+ → C，60+ → D，其余 → E
    if score >= 90:                    #★ 从高到低判断，顺序不能乱
        return 'A'

    elif score >= 80:                  #能走到这里，说明已经 < 90 了，不用再写 score < 90
        return 'B'

    elif score >= 70:
        return 'C'

    elif score >= 60:
        return 'D'

    else :                             #剩下的自然就是 60 以下
        return 'E'

# 蓝酱整理注释，代码一行没动
