def solution(order):
    answer = 0
    container = []
    for i in range(1, len(order) + 1):
        flag = 1
        while answer < i:
            if order[answer] == i:
                answer += 1
                flag = 0
            elif container and container[-1] == order[answer]:
                container.pop()
                answer += 1
                flag = 0
            else:
                break
        if flag:
            container.append(i)
    return answer
