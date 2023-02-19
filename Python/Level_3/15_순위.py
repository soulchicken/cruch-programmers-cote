def solution(n, results):
    answer = 0
    down = [[] for _ in range(n+1)]
    up = [[] for _ in range(n+1)]
    
    for win,lose in results:
        if lose not in down[win]:
            down[win].append(lose)
            
        if win not in up[lose]:
            up[lose].append(win)
    
    check = [1]*(n+1)
    check[0] = 0
    while 1:
        flag = 1
        for i in range(1,n+1):
            if check[i] and len(down[i]) + len(up[i]) == n-1:
                flag = 0
                check[i] = 0
            for d in down[i]:
                for u in up[i]:
                    if d not in down[u]:
                        down[u].append(d)
                    if u not in up[d]:
                        up[d].append(u)
                
        if flag:
            break
    return n - sum(check)