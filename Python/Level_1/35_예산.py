def solution(d, budget):
    answer = 0
    for i,v in enumerate(sorted(d)):
        if answer + v > budget: return i
        answer += v
    return i+1