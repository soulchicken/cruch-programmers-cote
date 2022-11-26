def solution(k, tangerine):
    dic = dict()
    for i in tangerine:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
    li = []
    for key, value in dic.items():
        li.append((value,key))
    li.sort()
    count = 0
    answer = 0
    while count < k:
        answer += 1
        val, _ = li.pop()
        count += val
    return answer