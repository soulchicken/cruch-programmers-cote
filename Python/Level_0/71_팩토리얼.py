def solution(n):
    m = 1
    for i in range(1,12):
        m *= i
        if m > n: return i-1