def solution(clothes):
    dic = dict()
    for _,j in clothes:
        if j in dic:
            dic[j] += 1
        else:
            dic[j] = 1
    answer = 1
    for value in dic.values():
        answer *= 1+value
    return answer - 1