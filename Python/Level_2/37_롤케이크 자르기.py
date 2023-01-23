def solution(topping):
    li1 = []
    left = set()
    for i in topping:
        left.add(i)
        li1.append(len(left))
    li2 = []
    right = set()
    for i in topping[::-1]:
        right.add(i)
        li2.append(len(right))
    li1.pop()
    li2.pop()
    li2 = li2[::-1]

    answer = 0
    for i in range(len(topping) - 1):
        if li1[i] == li2[i]:
            answer += 1

    return answer
