def solution(elements):
    LEN = len(elements)
    answer = set()
    elements += elements
    for i in range(LEN):
        t = 0
        for j in range(i, i + LEN):
            t += elements[j]
            answer.add(t)
    return len(answer)