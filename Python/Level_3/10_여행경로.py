def solution(tickets):
    DEPTH = len(tickets)
    tickets.sort()
    check = [1]*DEPTH
    stack = []

    def DFS(depth, start):
        if depth == DEPTH:
            stack.append(start)
            return
        for i in range(DEPTH):
            a, b = tickets[i]
            if check[i] and a == start:
                check[i] = 0
                stack.append(a)
                DFS(depth+1, b)
                if len(stack) > DEPTH:
                    return
                stack.pop()
                check[i] = 1
    DFS(0, "ICN")
    return stack
