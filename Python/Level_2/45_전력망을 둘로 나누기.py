def solution(n, wires):
    answer = 999
    li = [[] for _ in range(n+1)]
    for a, b in wires:
        li[a].append(b)
        li[b].append(a)

    from collections import deque
    que = deque()
    for a, b in wires:
        check = [0]*(n+1)
        count_box = []
        for i in range(1, n+1):
            if check[i]:
                continue
            count = 1
            que.append(i)
            while que:
                idx = que.pop()
                if check[idx]:
                    continue
                check[idx] = 1
                count += 1
                if idx == a:
                    for x in li[idx]:
                        if x != b:
                            que.append(x)
                elif idx == b:
                    for x in li[idx]:
                        if x != a:
                            que.append(x)
                else:
                    for x in li[idx]:
                        que.append(x)

            count_box.append(count)
            if len(count_box) > 2:
                break
        if len(count_box) == 2:
            answer = min(answer, abs(count_box[0] - count_box[1]))

    return answer
