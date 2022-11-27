def solution(n):
    li = [0]*n
    li[0] = 1
    li[1] = 2
    for i in range(2, n):
        li[i] = (li[i-1] + li[i-2]) % 1000000007
    return li[-1]