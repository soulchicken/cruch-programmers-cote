def solution(before, after):
    li = [0]*26
    for i in before: li[ord(i)-ord('a')] += 1
    for i in after: li[ord(i)-ord('a')] -= 1
    for i in li:
        if i != 0: return 0
    return 1