def solution(m, n, puddles):
    li = [[0]*(m+1) for _ in range(n+1)]
    for i,j in puddles:
        li[j][i] = -1
    li[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if li[i][j] != -1:
                if li[i][j-1] != -1:
                    li[i][j] += li[i][j-1]
                if li[i-1][j] != -1:
                    li[i][j] += li[i-1][j]
                li[i][j] %= 1000000007
    return li[-1][-1]