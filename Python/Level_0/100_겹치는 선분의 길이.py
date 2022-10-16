def solution(lines):
    li = [0]*300
    for i,j in lines:
        x,y = min(i,j),max(i,j)
        for n in range(x,y):
            li[n - 105] += 1
    answer = 0
    for i in li:
        if i > 1: answer += 1
    return answer