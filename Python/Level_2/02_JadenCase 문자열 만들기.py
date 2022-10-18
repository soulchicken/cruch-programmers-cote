def solution(s):
    return ''.join(s[i].upper() if not i or s[i-1] == ' ' else s[i].lower() for i in range(len(s)))