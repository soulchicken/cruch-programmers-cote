def solution(n):
    li = [0]*(n+1)
    li[1] = 1
    for i in range(2,n+1): li[i] = (li[i-1] + li[i-2])%1234567
    return li[-1]