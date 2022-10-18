def solution(s):
    r,l = 0,0
    for i in s:
        if i == '(': l += 1
        else: r += 1
        if r > l:return False
    return r==l