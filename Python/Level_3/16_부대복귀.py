def solution(n, roads, sources, destination):
    INF = float('inf')
    li = [INF]*(n+1)
    road = [[] for _ in range(n+1)]
    for a,b in roads:
        road[a].append(b)
        road[b].append(a)
    
    from collections import deque
    que = deque()
    que.append((0,destination)) # count, index
    
    while que:
        count, index = que.popleft()
        if li[index] <= count:
            continue
        li[index] = count
        count += 1
        for i in road[index]:
            que.append((count,i))
    
    answer = []
    for s in sources:
        count = li[s]
        if count == INF:
            answer.append(-1)
        else:
            answer.append(li[s])
    
    return answer