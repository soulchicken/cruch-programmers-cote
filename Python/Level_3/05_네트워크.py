def solution(n, computers):
    from collections import deque
    answer = 0
    check = [0]*n
    que = deque()
    for i in range(n):
        if check[i]: continue
        answer += 1
        que.append(i)
        while que:
            x = que.pop()
            if check[x]:
                continue
            check[x] = 1
            for j in range(n):
                if computers[x][j]:
                    que.append(j) 
    return answer