def solution(score):
    score = sorted([[sum(val), idx] for idx,val in enumerate(score)])
    print(score)
    answer = [0]*len(score)
    stack = 1
    num = -1
    i = 0
    while score:
        val,idx = score.pop()
        if val != num:
            num = val
            answer[idx] = stack
            stack += 1
            i = idx
        else:
            stack += 1
            answer[idx] = answer[i]
    return answer