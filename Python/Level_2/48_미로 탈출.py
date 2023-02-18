def solution(maps):
    from collections import deque
    
    I = len(maps)
    J = len(maps[0])
    INF = float('inf')
    
    def CHECK(i,j):
        return (0 <= i < I and 0 <= j < J)
    
    li1 = [[INF]*J for _ in range(I)]
    li2 = [[INF]*J for _ in range(I)]

    move = ((1,0),(-1,0),(0,1),(0,-1))
    
    for i in range(I):
        for j in range(J):
            if maps[i][j] == 'X':
                li1[i][j] = 0
                li2[i][j] = 0
            elif maps[i][j] == 'S':
                si, sj = i,j
            elif maps[i][j] == 'L':
                li, lj = i,j
            elif maps[i][j] == 'E':
                ei, ej = i,j
    
    
    que = deque()
    que.append((si,sj,0)) # 좌표i, 좌표j, count
    answer1 = -1
    
    while que:
        i,j,count = que.popleft()
        if i == li and j == lj:
            answer1 = count
            break
        if not CHECK(i,j) or li1[i][j] <= count:
            continue
        li1[i][j] = count
        for x,y in move:
            que.append((i+x,j+y, count+1))
    
    if answer1 == -1:
        return -1
    
    que = deque()
    que.append((li, lj, 0))
    answer2 = -1
    
    while que:
        i,j,count = que.popleft()
        if i == ei and j == ej:
            answer2 = count
            break
        if not CHECK(i,j) or li2[i][j] <= count:
            continue
        li2[i][j] = count
        for x,y in move:
            que.append((i+x,j+y, count+1))
    if answer2 == -1:
        return -1
    return answer1 + answer2