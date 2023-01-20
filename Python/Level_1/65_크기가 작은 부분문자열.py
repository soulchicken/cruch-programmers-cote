def solution(t, p):
    answer = 0
    P = len(p)
    pNum = int(p)
    for i in range(len(t) - len(p) + 1):
        if int(t[i:i+P]) <= pNum:
            answer += 1
    return answer
