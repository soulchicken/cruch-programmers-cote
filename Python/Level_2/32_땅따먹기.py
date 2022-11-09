def solution(land):
    for i in range(len(land)-1):
        for j in range(4):
            n = 0
            for k in range(4):
                if j != k and n < land[i][k]:
                    n = land[i][k]
            land[i+1][j] += n
    return max(land[-1])