def solution(X, Y):
    li1 = [0]*10
    li2 = [0]*10
    for i in X:
        li1[int(i)] += 1
    for i in Y:
        li2[int(i)] += 1
    for i in range(10):
        li1[i] = min(li1[i],li2[i])
    answer = ''
    count = 0
    for i in range(9,-1,-1):
        if li1[i] == 0 and i != 0: count += 1
        answer += str(i) * li1[i]
    if not answer: return "-1"
    if count == 9: return "0"
    return answer