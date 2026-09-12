def average(scores):
    # TODO: 在这里写你的代码
    res = sum(scores)/len(scores)
    res = round(res,1)
    return res


def grade(score):
    # TODO: 在这里写你的代码
    if score >= 90:
        return 'A'

    elif score >= 80:
        return 'B'

    elif score >= 70:
        return 'C'

    elif score >= 60:
        return 'D'

    else :
        return 'E'