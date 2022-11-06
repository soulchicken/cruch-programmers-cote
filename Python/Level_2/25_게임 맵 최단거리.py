def solution(maps):
    I, J = len(maps), len(maps[0])
    count_map = [[float('inf')]*J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            if not maps[i][j]:
                count_map[i][j] = 0

    from collections import deque
    que = deque([[0, 0, 1]])  # i,j, count
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while que:
        i, j, count = que.popleft()
        if 0 <= i < I and 0 <= j < J and count_map[i][j] > count:
            count_map[i][j] = count
            for x, y in move:
                que.append([i+x, j+y, count+1])
    return count_map[-1][-1] if count_map[-1][-1] != float('inf') else -1
