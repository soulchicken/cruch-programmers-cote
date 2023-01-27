def solution(n, s):
    answer = [s//n]*n
    k = s % n
    for i in range(k):
        answer[i] += 1
    for i in answer:
        if not i:
            return [-1]
    return answer[::-1]
