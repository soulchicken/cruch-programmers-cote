def solution(maps):
    from collections import deque
    answer = []
    I = len(maps)
    J = len(maps[0])
    li = [[0 for _ in range(J)] for _ in range(I)]

    def check(i, j):
        return 0 <= i < I and 0 <= j < J
    move = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for i in range(I):
        for j in range(J):
            if maps[i][j] == 'X':
                li[i][j] = 1

    for i in range(I):
        for j in range(J):
            if li[i][j]:
                continue

            count = 0
            que = deque()
            que.append((i, j))

            while que:
                a, b = que.pop()
                if not check(a, b):
                    continue
                if li[a][b]:
                    continue
                count += int(maps[a][b])
                li[a][b] = 1

                for x, y in move:
                    que.append((x+a, y+b))
            answer.append(count)

    if answer:
        return sorted(answer)
    return [-1]
