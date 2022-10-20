def solution(s):
    a,b = 0,0
    while s != '1':
        a += 1
        b += s.count('0')
        s = bin(len(s.replace('0','')))[2:]
    return [a,b]