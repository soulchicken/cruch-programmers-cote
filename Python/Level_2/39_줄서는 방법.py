def solution(n, k):
    answer = []
    x = 1
    li = [i for i in range(1, n+1)]
    x_li = []
    for i in range(1, n):
        x *= i
        x_li.append(x)

    for y in range(n-1, 0, -1):
        x = x_li.pop()
        idx = k // x
        k %= x
        if k:
            answer.append(li.pop(idx))
        else:
            answer.append(li.pop(idx - 1))

    answer.append(li.pop())
    return answer
