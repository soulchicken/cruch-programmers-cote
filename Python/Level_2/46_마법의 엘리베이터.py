def solution(storey):
    from collections import deque
    que = deque()
    que.append((0, storey))
    answer = float('INF')
    while que:
        count, storey = que.popleft()

        if not storey:
            answer = min(count, answer)
            continue
        n = storey % 10
        if n == 5:
            que.append((count+5, storey // 10))
            que.append((count+5, 1 + storey // 10))
        elif n < 5:
            que.append((count+n, storey // 10))
        else:
            que.append((count+10-n, 1 + storey // 10))

    return answer
