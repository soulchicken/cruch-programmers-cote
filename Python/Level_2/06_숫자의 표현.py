def solution(n):
    answer = 0
    for i in range(1,n+1):
        t = 0
        for j in range(i,n+1):
            if t + j < n:
                t += j
                continue
            if t + j == n:
                answer += 1
            break
    return answer