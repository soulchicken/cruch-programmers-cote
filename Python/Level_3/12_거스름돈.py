def solution(n, money):
    answer = 0
    li = [0]*(n+1)
    li[0] = 1
    for m in money:
        for i in range(m, n+1):
            li[i] = (li[i] + li[i-m]) % 1000000007
    return li[-1]
