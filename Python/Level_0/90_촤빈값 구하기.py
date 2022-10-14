def solution(array):
    s = dict()
    for i in array:
        if i in s: s[i] += 1
        else: s[i] = 1
    s = sorted([[val,key] for key, val in s.items()])
    if len(s) != 1 and s[-1][0] == s[-2][0]: return -1
    return s[-1][1]