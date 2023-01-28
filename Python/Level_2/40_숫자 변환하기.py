def solution(x, y, n):
    from collections import deque
    que = deque()
    que.append((0, x))  # n번, 현재 숫자
    check = [float('inf')]*(y+1)

    while que:
        count, num = que.popleft()
        if num > y:
            continue
        if check[num] > count:
            check[num] = count
            que.append((count+1, num+n))
            que.append((count+1, num*2))
            que.append((count+1, num*3))

    return -1 if check[y] == float('inf') else check[y]
