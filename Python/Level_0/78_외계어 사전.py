def solution(spell, dic):
    for i in dic:
        flag = True
        for j in spell:
            if j not in i:flag = False
        if flag:return 1
    return 2