def solution(name, yearning, photo):
    answer = []
    dic = dict()
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for pho in photo:
        total = 0
        for man in pho:
            if man in dic:
                total += dic[man]
        answer.append(total)

    return answer
