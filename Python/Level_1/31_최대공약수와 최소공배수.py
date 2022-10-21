def solution(n, m):
    for i in range(max(n,m),0,-1):
        if not n%i + m%i: return [i,n*m//i]